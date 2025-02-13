import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Bug: The condition will always be False
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Create and place the password label and entry
label_password = tk.Label(root, text="Password")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

# Run the application
root.mainloop()