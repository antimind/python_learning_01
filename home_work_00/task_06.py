contacts = []
isExit = False
while not isExit:
    action = input("1. Add contact\n2. View contacts\n3. Exit\n")
    match action:
        case "1":
            name = input("> Enter contact name: ")
            phoneNumber = input("> Enter a phone number: ")
            if name != "" and phoneNumber != "":
                contacts.append([name, phoneNumber])
        case "2":
            if len(contacts) == 0:
                print("> No contacts found")
            else:
                print(" *****")
                for contact in contacts:
                    print(f" - Name: {contact[0]}, Phone Number: {contact[1]}")
                print(" *****")
        case "3":
            isExit = True
        case _:
            print("Invalid input")