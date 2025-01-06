import bcrypt

def encrypt_password(password):
    """
    Hashes a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    """
    Verifies a password against its hash.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
