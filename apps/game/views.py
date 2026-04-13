from django.shortcuts import render
from apps.game.GameController import GameController
from apps.game.models import GameResult

def signal_game_start(request, input_func = input):
    user_id = request.session.get('user_id')
    gamemode = input_func("Enter gamemode (easy/hard): ")
    game_controller = GameController(gamemode, user_id)
    game_result = game_controller.GameStart()
    
    # Save the game result to the database
    game_result.save()