import re

def check_password_policy(password):
    """
    Determines if a password is strong or weak and provides suggestions.
    """
    suggestions = []
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Password should include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Password should include at least one lowercase letter.")
    if not re.search(r"\d", password):
        suggestions.append("Password should include at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Password should include at least one special character.")
    
    if suggestions:
        return "Weak", suggestions
    return "Strong", ["Password meets all strength criteria."]
