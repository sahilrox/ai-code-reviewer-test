import hashlib

SECRET_KEY = "mySecretKey123"  # hardcoded secret

def login(username, password):
    if username == "admin" and password == "admin":  # hardcoded creds
        return True
    return False

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # md5 is insecure

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + str(user_id)  # sql injection
    return query
