import csv
import os

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if user already exists
    if user_exists(username):
        print("Username already exists. Please choose a different username.")
        return

    # Save user to CSV
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    
    print("User registered successfully!")

def user_exists(username):
    if not os.path.exists('users.csv'):
        return False
    
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login successful!")
                return
    print("Invalid username or password.")

def main():
    print("Welcome to the User System")
    while True:
        action = input("Type 'register' to register, 'login' to log in, or 'exit' to quit: ").strip().lower()
        if action == 'register':
            register_user()
        elif action == 'login':
            login_user()
        elif action == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
