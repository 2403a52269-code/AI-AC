import os
import hashlib

# Simulated user database (in-memory)
user_db = {}

def hash_password(password):
    # Simple SHA-256 hashing
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    hashed = hash_password(password)
    user_db[username] = hashed

def login(username, password):
    hashed = user_db.get(username)
    if not hashed:
        return False
    return hashed == hash_password(password)

if __name__ == "__main__":
    # Registration
    username = input("Enter username to register: ")
    password = input("Enter password to register: ")
    register(username, password)
    print(f"User '{username}' registered.")

    # Login
    login_username = input("Enter username to login: ")
    login_password = input("Enter password to login: ")
    if login(login_username, login_password):
        print("Login successful!")
    else:
        print("Login failed.")
