import string

class PasswordSecurity:
    @staticmethod
    def validate_password(password):
        # Check if password length is at least 12 characters
        if len(password) < 12:
            return False
        
        # Check if password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False
        
        # Check if password contains at least one special character
        special_chars = string.punctuation
        if not any(char in special_chars for char in password):
            return False
        
        # Check if password contains only allowed characters
        allowed_chars = string.ascii_letters + string.digits + string.punctuation
        if not all(char in allowed_chars for char in password):
            return False
        
        # Check if password contains no spaces
        if ' ' in password:
            return False
        
        return True
