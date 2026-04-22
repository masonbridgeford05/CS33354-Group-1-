from django.test import TestCase, Client
from apps.accounts.models import User
from apps.game.models import GameImage, GameResult
from django.urls import reverse

class CometGridIntegrationTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        # Use our custom creation logic
        self.test_user = User.createUserAccount(
            userName="Temoc", 
            userEmail="temoc@utdallas.edu", 
            userPassword="password12345"
        )
        self.test_image = GameImage.objects.create(
            location="Student Union", 
            difficulty=0, 
            image_path="test_image.jpg"
        )

    def test_full_user_workflow(self):
        # 1. Login
        login_data = {'userEmail': 'temoc@utdallas.edu', 'userPassword': 'password12345'}
        self.client.post(reverse('login'), login_data)
        
        # 2. Check session
        self.assertEqual(self.client.session['user_id'], self.test_user.userId)

        # 3. Play Game (using the correct URL name)
        # Added 'difficulty' to ensure the view can save 'gamemode' to the DB
        game_data = {
            'guess': 'Student Union', 
            'difficulty': 'easy'
        }
        
        # We need to set the session 'game_answer' so the view has something to compare
        session = self.client.session
        session['game_answer'] = 'Student Union'
        session.save()

        response = self.client.post(reverse('signal_game_start'), game_data)

        # 4. Verify DB update
        updated_results = GameResult.objects.filter(user_id=self.test_user)
        self.assertEqual(updated_results.count(), 1, "GameResult was not saved to the database.")
        
        # Optional: check if the score was actually recorded
        self.assertGreater(updated_results.first().score, 0)