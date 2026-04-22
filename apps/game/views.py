from django.shortcuts import render, redirect
from apps.game.GameController import GameController
from apps.game.models import GameResult
from apps.accounts.models import User
from apps.leaderboard.LeaderboardController import LeaderboardController

def signal_game_start(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('login')

    if request.method == "POST":
        user_guess = request.POST.get('guess')
        answer = request.session.get('game_answer')
        
        mode_input = request.POST.get('difficulty') or request.session.get('game_mode') or 'easy'
        mode_val = 0 if mode_input == 'easy' else 1
        
        game_controller = GameController(mode_val, user_id)
        
        # Capture the result object returned by the controller
        game_result = game_controller.GameStart(input_func=lambda x: user_guess, answer=answer)
        
        # Link User and Save Game Result
        user_obj = User.objects.get(userId=user_id) 
        game_result.user_id = user_obj
        game_result.gamemode = mode_input 
        game_result.save()

        # Save to Leaderboard using the game_result object
        leaderboard_ctrl = LeaderboardController()
        leaderboard_ctrl.save_score(user_id, game_result)
        
        return render(request, 'dashboard.html', {'score': game_result.score})
    
    return render(request, 'game.html')