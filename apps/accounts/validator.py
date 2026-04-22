class Validator:
    @staticmethod
    def isValidEmail(email):
        if not email or not isinstance(email, str):
            return False
        if not email.endswith("@utdallas.edu"):
            return False
        email_parts = email.split('@')
        # Check if there is a prefix before the @
        return len(email_parts[0]) > 0
    
    @staticmethod
    def isValidPassword(password):
        # Checks if password exists and meets the 12-character requirement
        if password and isinstance(password, str):
            return len(password) >= 12
        return False