import hashlib

def hash_password(password):
    """
    Encrypts string

    Args:
        password(str)

    Returns:
        string
    """

    password = password.encode('utf-8')
    hasher = hashlib.sha1()
    hasher.update(password)
    return hasher.hexdigest()

