import random
from django.shortcuts import render, redirect
from apps.game.GameController import GameController
from apps.game.models import GameResult, GameImage 
from apps.accounts.models import User
from apps.leaderboard.LeaderboardController import LeaderboardController

def signal_game_start(request):
    """
    Handles the core gameplay loop including attempt tracking, 
    image display, and score finalization.
    """
    user_id = request.session.get('user_id')
    
    #Authenticate user before proceeding
    if not user_id:
        return redirect('login')

    #Initialize attempts in session if starting fresh
    if 'attempts' not in request.session:
        request.session['attempts'] = 0

    # Processing a Guess
    if request.method == "POST":
        user_guess = request.POST.get('guess')
        answer = request.session.get('game_answer')
        
        # Increment attempt counter 
        request.session['attempts'] += 1
        current_attempts = request.session['attempts']
        
        mode_input = request.POST.get('difficulty') or request.session.get('game_mode') or 'easy'
        mode_val = 0 if mode_input == 'easy' else 1
        
        game_controller = GameController(mode_val, user_id)
        
        game_result = game_controller.GameStart(input_func=lambda x: user_guess, answer=answer)

        if game_result.score > 0:
            # Calculate scores based on the number of attempts
            if current_attempts == 1:
                game_result.score = 3000
            elif current_attempts == 2:
                game_result.score = 2000
            elif current_attempts == 3:
                game_result.score = 1000
            
            # Finalize Score and link to User
            user_obj = User.objects.get(userId=user_id) 
            game_result.user_id = user_obj
            game_result.gamemode = mode_input 
            game_result.save()

            # Update Leaderboard rankings
            leaderboard_ctrl = LeaderboardController()
            leaderboard_ctrl.save_score(user_id, game_result)
            
            # Clear game-specific session data
            request.session['attempts'] = 0
            if 'game_answer' in request.session:
                del request.session['game_answer']

            return render(request, 'dashboard.html', {'score': game_result.score})
        
        #If incorrect and attempts < 3, allow another attempt and enlarge image
        else:
            return render(request, 'game.html', {
                'image_url': request.session.get('current_image_url'),
                'enlarge_image': True, 
                'location_hint': f"Incorrect. Attempt {current_attempts}/3. Try again!"
            })
    # select campus images
    all_images = GameImage.objects.all()
    
    if not all_images:
        # Prevents ValueError by ensuring an HttpResponse is always returned
        return render(request, 'game.html', {'error': 'No images found in database.'})

    # Randomly select a challenge for the session
    random_image = random.choice(all_images)
    
    # Store challenge data in session for comparison in POST
    request.session['game_answer'] = random_image.location
    request.session['current_image_url'] = random_image.image_path.url
    request.session['attempts'] = 0 
    
    context = {
        'image_url': random_image.image_path.url,
        'location_hint': "Can you guess where this is on campus?",
        'enlarge_image': False
    }
    
    return render(request, 'game.html', context)