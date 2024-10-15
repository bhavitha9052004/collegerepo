import csv
import os
import sys

def register_user(username, password):
    if user_exists(username):
        print("Username already exists. Please choose a different username.")
        return False

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    
    print("User registered successfully!")
    return True

def user_exists(username):
    if not os.path.exists('users.csv'):
        return False
    
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False

def login_user(username, password):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login successful!")
                return True
    print("Invalid username or password.")
    return False

def main():
    if len(sys.argv) < 4:
        print("Usage: python login.py <action> <username> <password>")
        return

    action = sys.argv[1].lower()
    username = sys.argv[2]
    password = sys.argv[3]

    if action == 'register':
        register_user(username, password)
    elif action == 'login':
        login_user(username, password)
    else:
        print("Invalid action. Use 'register' or 'login'.")

if __name__ == "__main__":
    main()

