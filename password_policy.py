import re

def check_password_policy(password):
    """
    Determines if a password is strong or weak.
    Strong password criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one number
    - Contains at least one special character
    """
    if len(password) < 8:
        return "Weak"
    if not re.search(r"[A-Z]", password):
        return "Weak"
    if not re.search(r"[a-z]", password):
        return "Weak"
    if not re.search(r"\d", password):
        return "Weak"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak"
    return "Strong"
