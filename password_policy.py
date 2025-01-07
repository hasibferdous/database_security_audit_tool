import re

def check_password_policy(password):
    """
    Determines if a password is strong or weak.
    Suggests improvements for weak passwords.
    """
    suggestions = []
    if len(password) < 8:
        suggestions.append("Increase length to at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Add at least one lowercase letter.")
    if not re.search(r"\d", password):
        suggestions.append("Include at least one numeric digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Include at least one special character.")

    if suggestions:
        return "Weak", suggestions
    return "Strong", []
