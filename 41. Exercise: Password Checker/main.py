from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")
password_length = str(len(password))
password_stars = "*" * len(password)

print(f"{username}, your password {password_stars} is {password_length} letters long.")
