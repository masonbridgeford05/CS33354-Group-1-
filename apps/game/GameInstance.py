class GameInstance:
    # Moved gameID to the game object
    def __init__(self, gamemode):
        # print("GameInstance Initialize 1\n")
        self.gamemode = gamemode
        self.score = 0
        self.attempts = 0
        # print("GameInstance Initialize 2\n")
        self.valid_modes = ["easy", "hard", 1]

    def getScore(self):
        # print("GameInstance getScore \n")
        return self.score

    def calculateScore(self):
        # print("GameInstance CalculateScore 1\n")
        if self.gamemode == 1 or self.gamemode == "hard":
            # print("GameInstance CalculateScore 2 Hard\n")
            self.score = (3 - self.attempts) * (2) * (1000)
        else: 
            # print("GameInstance CalculateScore 2 Easy\n")
            self.score = (3 - self.attempts) * (1000)

    def getattempts(self):
        # print("GameInstance getattempts \n")
        return self.attempts

    def incrementAttempts(self):
        # print("GameInstance incrementAttempts \n")
        self.attempts += 1

    def is_valid_mode(self):
        return self.gamemode in self.valid_modes

    def is_valid_input(self, user_input):
        return user_input is not None and user_input != ""

# Replaced gamestart, will handle game play loop in controller
    def evaluate(self, user_input, answer):
        # print("GameInstance evaluate 1\n")

        if not self.is_valid_mode():
            raise ValueError("Invalid game mode")

        if not self.is_valid_input(user_input):
            self.attempts += 1
            return False

        if (user_input == answer): # Evaluates the user input against the correct answer
            # Updates the score and returns true if they are equal
            # print("GameInstance evaluate 2 Correct\n")
            self.calculateScore()
            return True
        else:
            # Increments the number of attempts and returns false otherwise
            # print("GameInstance evaluate 2 Incorrect\n")
            self.attempts += 1
            return False