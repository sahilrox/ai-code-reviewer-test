import os

def divide(a, b):
    return a / b  # bug: no zero division check

def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id  # bug: SQL injection
    return query

password = "admin123"  # bug: hardcoded secret

def process_list(items):
    result = []
    for i in range(len(items)):  # suggestion: use enumerate
        result.append(items[i] * 2)
    return result

def connect():
    db = os.getenv("DB_URL")
    print("Connecting to: " + db)  # warning: leaking connection string
