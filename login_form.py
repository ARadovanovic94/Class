def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Bug: The condition will always be False
    if username == "admin" and password == "password123":
        print("Login successful")
    else:
        print("Invalid username or password")

# Simulate the main loop
while True:
    login()
    again = input("Do you want to try again? (yes/no): ")
    if again.lower() != "yes":
        break