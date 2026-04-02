from PIL import Image


class GameInstance:
    
    def __init__(self, gamemode):
        self.score = 0
        self.gamemode = gamemode
        self.attempts = 0
    
    def startGame(self, gamemode, image_path, answer):
        self
        