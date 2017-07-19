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


def hash(content):
    """
    Encrypt string with Caesar cipher

    Args:
        content (str)
    """

    content = chr(ord(content)-3)

    return content


def dehash(content):
    """
    Encrypt string with Caesar cipher

    Args:
        content (str)
    """

    content = chr(ord(content)+3)

    return content
