menuOption = 0
form = {}

while menuOption != 4:
    print("\nREGISTRATION FORM")
    print("1 - Add information to the form")
    print("2 - Retrieve information from the form")
    print("3 - Display the complete form")
    print("4 - Exit")
    menuOption = int(input("Enter your choice: "))

    if menuOption == 1:
        key = input("Specify the field you wish to add to the form: ")
        value = input("Enter the information you wish to register in the form: ")
        form.update({key: value})

    elif menuOption == 2:
        print(f"The fields available on the form are {form.keys()} ")
        key = input("Please specify which field you would like to display: ")

        if key in form.keys():
            print(f"The field {key} contains the data {form.get(key)}")
        else:
            print("Invalid Option")

    elif menuOption == 3:
        print("REGISTRATION FORM")
        for field, data in form.items():
            print(f"{field.upper()} -> {data}")

    elif menuOption == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Option")
