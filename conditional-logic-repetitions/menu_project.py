userName = input("Please enter your name: ")
optionMenu = 0

while optionMenu != 3:
    print("1 - To be welcomed!")
    print("2 - Calculate factorial")
    print("3 - Exit")
    optionMenu = int(input("Please enter your choice: "))

    if optionMenu == 1:
        print(f"Welcome, {userName}!")
    elif optionMenu == 2:
        numberFact = int(input("Please enter a number: "))
        factorial = numberFact

        for value in range(1, numberFact, 1):
            factorial *= value

        print(f"The factorial of {numberFact} is {factorial}")
    elif optionMenu == 3:
        print("Exiting menu...")
    else:
        print("Choose a menu option")