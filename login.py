def login():
    print("login")
    username = input("username: ")
    password = input("Password: ")


    try:
        with open("users.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Account not found. Register to create an account")
        return
    
    for line in lines:
        stored_username, stored_password = line.strip().split(", ")
        if username == stored_username and password == stored_password:


print("Please enter an option")
print("1. Already have an account? Login")
print("2 .Dont have an account? Register")
print("3. Exit")

choice = input("Enter your choice(1/2/3): ")

if choice == "1":
    print("Please enter login details")
elif choice == "2":
    print("Please register your account")
elif choice == "3":
    print("Exiting Goodbye!")
    
else:
    print("Invalid")
def register():
    print("Register! ")
    username = input("username: ")
    password = input("password: ")
    confirm = input("confirm password: ")

    if password != confirm:
        print("Password does not match. ")

    with open("users.txt", "a") as file:
        file.write(f"{username}, {password}")

    print("Registration successful! Please login below")
    login() 