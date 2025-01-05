import re

# Validate mobile function
def validate_mobile(phone):
    pattern = r"^01[0-2,5]\d{8}$"  # Matches Egyptian mobile numbers
    return re.fullmatch(pattern, phone)

# Validate email function
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.fullmatch(pattern, email)

# Registration function
def register(users):
    print("Register:")
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    password = input("Enter Password: ").strip()
    confirm_password = input("Confirm Password: ").strip()
    email = input("Enter Email: ").strip()
    mobile = input("Enter Mobile: ").strip()

    if not validate_email(email):
        print("Invalid email format.")
        return

    if email in users:
        print("Email already registered.")
        return

    if not validate_mobile(mobile):
        print("Invalid mobile number.")
        return

    if password != confirm_password:
        print("Passwords do not match.")
        return

    users[email] = {
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
        "mobile": mobile,
    }
    print("Registration Successful!")

# Login function
def login(users):
    print("Login:")
    email = input("Enter Email: ").strip()
    password = input("Enter Password: ").strip()

    if email in users and users[email]["password"] == password:
        print(f"Welcome back, {users[email]['first_name']}!")
        return True
    else:
        print("Login Failed: Invalid email or password.")
        return False

# Main loop
users = {}
while True:
    _input = input("Register or Login (or Exit): ").strip().lower()

    if _input == "exit":
        print("Exiting program. Goodbye!")
        break
    elif _input == "register":
        register(users)
    elif _input == "login":
        if login(users):
            break
    else:
        print("Invalid input. Please enter 'Register', 'Login', or 'Exit'.")
