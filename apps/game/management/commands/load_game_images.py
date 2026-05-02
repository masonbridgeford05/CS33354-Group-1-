from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from pathlib import Path
from apps.game.models import GameImage
import os

class Command(BaseCommand):
    help = 'Load images from Easy and Hard subdirectories into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing images before loading'
        )

    def handle(self, *args, **options):
        clear_existing = options['clear']

        if clear_existing:
            GameImage.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared existing images'))

        # Path to GameImages folder in media
        base_path = Path(__file__).resolve().parent.parent.parent.parent.parent / 'media' / 'GameImages'
        
        if not base_path.exists():
            self.stdout.write(self.style.ERROR(f'GameImages folder not found at {base_path}'))
            return

        # Define difficulty directories
        difficulty_dirs = {
            'easy': base_path / 'Easy',
            'hard': base_path / 'Hard'
        }

        image_extensions = {'.jpg', '.jpeg', '.png', '.gif'}
        created_count = 0
        skipped_count = 0

        # Process each difficulty level
        for difficulty, dir_path in difficulty_dirs.items():
            if not dir_path.exists():
                self.stdout.write(self.style.WARNING(f'{difficulty.capitalize()} directory not found'))
                continue

            # Get all image files in this directory
            image_files = [f for f in dir_path.iterdir() 
                          if f.is_file() and f.suffix.lower() in image_extensions]

            if not image_files:
                self.stdout.write(self.style.WARNING(f'No image files found in {difficulty.capitalize()} folder'))
                continue

            self.stdout.write(f'\nProcessing {difficulty.upper()} images...')

            for image_file in image_files:
                # Use filename without extension as location name
                location_name = image_file.stem
                
                # Check if image already exists
                if GameImage.objects.filter(location=location_name, difficulty=difficulty).exists():
                    self.stdout.write(f'  ⊘ Skipping {image_file.name} (already exists)')
                    skipped_count += 1
                    continue

                try:
                    # Create GameImage entry
                    game_image = GameImage(
                        difficulty=difficulty,
                        location=location_name
                    )
                    
                    # Read and save the image file
                    with open(image_file, 'rb') as img:
                        game_image.image_path.save(
                            image_file.name,
                            ContentFile(img.read()),
                            save=True
                        )
                    
                    self.stdout.write(
                        self.style.SUCCESS(f'  ✓ Added {image_file.name} as "{location_name}" ({difficulty})')
                    )
                    created_count += 1
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'  ✗ Error loading {image_file.name}: {str(e)}')
                    )

        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Summary: {created_count} images added, {skipped_count} skipped')
        )
