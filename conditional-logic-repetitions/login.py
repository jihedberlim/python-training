userLogin = input("Please, enter the user who wishes to access the system: ")
userPassword = input("Please, Enter the password for the user who wishes to access the system: ")

if userLogin.upper() == "ADMIN" and userPassword == "123456":
    print(f"Welcome, {userLogin.upper()}!")
else:
    print("Username or password is incorrect. Access denied.")