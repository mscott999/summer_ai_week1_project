from  social_network_classes import SocialNetwork,Person
import social_network_ui

socialNetwork = SocialNetwork()

while (True):
    #Initiate main menu.
    choice = social_network_ui.mainMenu()

    #1a. Create a new account.
    if (choice == "1"):
        print("\nNew Account\n")
        while (True):
            name = input("Name: ")
            if (len(name) == 0):
                print("Error: no name given.")
            else:
                break
        while (True):
            age = input("Age: ")
            if (len(age) == 0):
                print("Error: no age given.")
            elif (age.isnumeric() == False):
                print ("Error: invalid age given.")
            else:
                break
        socialNetwork.createAccount(Person(name, age))
        print("\nAccount successfully created.")

    #2a. Manage my account.
    elif (choice == "2"):
        if (len(socialNetwork.personList) == 0):
            print("\nError: no accounts registered.")
        else:
            print("\nRegistered Accounts")
            for person in socialNetwork.personList:
                print(person.name)
            print("")
            while (True):
                signedInUser = None
                selectedName = input("Name of account: ")
                for person in socialNetwork.personList:
                    if (selectedName == person.name):
                        signedInUser = person
                if (signedInUser == None):
                    print("Error: ivalid name given.")
                else:
                    break
            print("\nCurrently signed in as", signedInUser.name, end = ".\n")
            while (True):
                #Initiate sub menu.
                choice2 = social_network_ui.manageAccountMenu()

                #1b. Edit my details.
                if (choice2 == "1"):
                    pass

                #2b. Add a friend.
                elif (choice2 == "2"):
                    pass

                #3b. View all my friends
                elif (choice2 == "3"):
                    pass

                #4b. View all my messages.
                elif (choice2 == "4"):
                    pass

                #5b. Go back.
                elif (choice2 == "5"):
                    break

                #Otherb.
                else:
                    print("Error: invalid number given")

    #3a. Quit.
    elif (choice == "3"):
        print("\nHave a great day!")
        break

    #Othera.
    else:
        print("Error: invalid number given")
