from django.shortcuts import render, redirect
from apps.game.GameController import GameController
from apps.game.models import GameResult
from apps.accounts.models import User

def signal_game_start(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('login')

    if request.method == "POST":
        user_guess = request.POST.get('guess')
        
        # Retrieve state from session or POST
        answer = request.session.get('game_answer')
        
        # Pull difficulty from POST to ensure we have a valid gamemode string
        mode_input = request.POST.get('difficulty') or request.session.get('game_mode') or 'easy'
        
        # Instantiate Controller with current user context
        # (Assuming GameController takes 0/1 for mode, we map 'easy' to 0)
        mode_val = 0 if mode_input == 'easy' else 1
        game_controller = GameController(mode_val, user_id)
        
        # GameStart should internally call game_instance.evaluate()
        # and return a GameResult object
        game_result = game_controller.GameStart(input_func=lambda x: user_guess, answer=answer)
        
        # Link Foreign Key AND set required fields ---
        user_obj = User.objects.get(userId=user_id) 
        game_result.user_id = user_obj
        
        # Assign the gamemode string to satisfy the NOT NULL constraint
        game_result.gamemode = mode_input 
        
        game_result.save()
        
        return render(request, 'dashboard.html', {'score': game_result.score})
    
    # Optional: logic for GET request to show the game page
    return render(request, 'game.html')