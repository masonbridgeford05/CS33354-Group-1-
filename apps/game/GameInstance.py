class GameInstance:
    # Moved gameID to the game object
    def __init__(self, gamemode):
        self.gamemode = gamemode
        self.score = 0
        self.attempts = 0
        self.valid_modes = ["easy", "hard", 0, 1]

    def getScore(self):
        return self.score

    def calculateScore(self):
        if self.gamemode == 1 or self.gamemode == "hard":
            self.score = (3 - self.attempts) * (2) * (1000)
        else: 
            self.score = (3 - self.attempts) * (1000)

    def getattempts(self):
        return self.attempts

    def incrementAttempts(self):
        self.attempts += 1

    def is_valid_mode(self):
        return self.gamemode in self.valid_modes

    def is_valid_input(self, user_input):
        return user_input is not None and user_input != ""

    def evaluate(self, user_input, answer):
        if not self.is_valid_mode() or self.gamemode is None:
            raise ValueError("Invalid game mode")

        if not self.is_valid_input(user_input):
            self.incrementAttempts()
            return False

        if user_input.strip().lower() == answer.strip().lower():
            self.calculateScore()
            return True
        else:
            self.incrementAttempts()
            return False