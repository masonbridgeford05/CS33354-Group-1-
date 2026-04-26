import random
from django.shortcuts import render, redirect
from apps.game.GameController import GameController
from apps.game.models import GameResult, GameImage 
from apps.accounts.models import User
from apps.leaderboard.LeaderboardController import LeaderboardController
from datetime import date
from django.contrib import messages

def signal_game_start(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('login')

    # --- WORDLE CHECK: Has the user played today? ---
    # This looks for any GameResult (win or loss) created today
    already_played = GameResult.objects.filter(
        user_id=user_id, 
        date_played__date=date.today() 
    ).exists()

    if already_played:
        messages.info(request, "You've already played today!")
        return redirect('dashboard')

    if 'attempts' not in request.session:
        request.session['attempts'] = 0

    if request.method == "GET":
        selected_mode = request.GET.get('mode', 'easy') # Default to easy
        request.session['game_mode'] = selected_mode
        
        # Filter images by difficulty
        all_images = GameImage.objects.filter(difficulty=selected_mode)
        
        if not all_images:
            messages.error(request, f"No {selected_mode} images found!")
            return redirect('dashboard')

        random_image = random.choice(all_images)
        request.session['game_answer'] = random_image.location
        request.session['current_image_url'] = random_image.image_path.url
        request.session['attempts'] = 0 
        
        return render(request, 'game.html', {
            'image_url': random_image.image_path.url,
            'mode': selected_mode
        })

    if request.method == "POST":
        user_guess = request.POST.get('guess')
        answer = request.session.get('game_answer')
        
        request.session['attempts'] += 1
        current_attempts = request.session['attempts']
        
        mode_input = request.POST.get('difficulty') or request.session.get('game_mode') or 'easy'
        mode_val = 0 if mode_input == 'easy' else 1
        
        game_controller = GameController(mode_val, user_id)
        game_result = game_controller.GameStart(input_func=lambda x: user_guess, answer=answer)

        #Correct Guess
        if game_result.score > 0:
        # Determine base points based on attempts
            if current_attempts == 1: 
                base_score = 3000
            elif current_attempts == 2: 
                base_score = 2000
            elif current_attempts == 3: 
                base_score = 1000
            else:
                base_score = 0

        mode = request.session.get('game_mode', 'easy')
        multiplier = 2 if mode == 'hard' else 1

        if game_result.score > 0:
            # Calculate weighted score
            base_points = {1: 3000, 2: 2000, 3: 1000}.get(current_attempts, 0)
            final_score = base_points * multiplier
            
            # Save the result
            user_obj = User.objects.get(userId=user_id)
            GameResult.objects.create(
                user_id=user_obj, 
                score=final_score, 
                gamemode=mode
            )

            messages.success(request, f"Correct! You earned {final_score} points on {mode.upper()} mode!")
            return redirect('dashboard')
        
        # Incorrect Guess
        else:
            if current_attempts >= 3:
                user_obj = User.objects.get(userId=user_id)
                GameResult.objects.create(user_id=user_obj, score=0, gamemode=mode_input)
                
                request.session['attempts'] = 0
                if 'game_answer' in request.session: del request.session['game_answer']
                
                messages.info(request, "Out of attempts! Better luck tomorrow.")
                return redirect('dashboard')
            
            return render(request, 'game.html', {
                'image_url': request.session.get('current_image_url'),
                'enlarge_image': True, 
                'location_hint': f"Incorrect. Attempt {current_attempts}/3. Try again!"
            })

    all_images = GameImage.objects.all()
    if not all_images:
        return render(request, 'game.html', {'error': 'No images found in database.'})

    random_image = random.choice(all_images)
    request.session['game_answer'] = random_image.location
    request.session['current_image_url'] = random_image.image_path.url
    
    return render(request, 'game.html', {
        'image_url': random_image.image_path.url,
        'location_hint': "Can you guess where this is on campus?",
        'enlarge_image': False
    })
