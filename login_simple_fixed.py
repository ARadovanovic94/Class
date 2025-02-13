def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Bug is fixed by adding the correct password for the user
    if username == "admin" and password == "password123":
        print("Login successful")
    elif username == "user" and password == "user_password":
        print("Login successful")
    else:
        print("Invalid username or password")

# Simulate the main loop
while True:
    login()
    again = input("Do you want to try again? (yes/no): ")
    if again.lower() != "yes":
        break