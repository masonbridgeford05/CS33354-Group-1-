class GameInstance:
    # Moved gameID to the game object
    def init(self, gamemode, gameID):
        self.gamemode = gamemode
        self.gameID = gameID
        self.score = 0
        self.attempts = 0

    def getGameID(self):
        return self.gameID

    def getScore(self):
        return self.score

    def calculateScore(self):
        if self.gamemode == 1:
            self.score = (3 - self.attempts) * (2) * (1000)
        else: 
            self.score = (3 - self.attempts) * (1000)

    def getattempts(self):
        return self.attempts

    def incrementAttempts(self):
        self.attempts + 1

# Replaced gamestart, will handle game play loop in controller
    def evaluate(self, user_input, answer):

        if (user_input == answer): # Evaluates the user input against the correct answer
            # Updates the score and returns true if they are equal
            self.calculateScore(self)
            return True
        else:
            # Increments the number of attempts and returns false otherwise
            self.attempts += 1
            return False