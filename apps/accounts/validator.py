class Validator:
    @staticmethod
    def isValidEmail(email):
        if not email.endswith("@utdallas.edu"):
            return False
        emailBeginning = email.split('@')
        if len(emailBeginning[0]) > 0:
            return True
        return False

    @staticmethod
    def isValidPassword(password):
        if len(password) >= 12:
            return True
        return False
