import tkinter as tk
from tkinter import messagebox

def register_user():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    if not username or not password or not email:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    # Save the data (in practice, save it securely)
    with open("users.txt", "a") as file:
        file.write(f"{username},{password},{email}\n")

    messagebox.showinfo("Success", "Registration successful!")

# Create the main window
root = tk.Tk()
root.title("Registration Page")

# Create and place labels and entries
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Register button
btn_register = tk.Button(root, text="Register", command=register_user)
btn_register.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
