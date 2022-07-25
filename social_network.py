from  social_network_classes import SocialNetwork,Person
import social_network_ui

#Social Network for tracking all registered acounts.
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
            print("\nRegistered Accounts:")
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
                    print("Error: invalid name given.")
                else:
                    break
            print("\nCurrently signed in as", signedInUser.name, end = ".\n")
            while (True):
                #Initiate sub menu.
                choice2 = social_network_ui.manageAccountMenu()

                #1b. Edit my details.
                if (choice2 == "1"):
                    print("\nEdit Details")
                    print("\nName:", signedInUser.name, "\nAge:", signedInUser.age)
                    print("")
                    while (True):
                        name = input("New name: ")
                        if (len(name) == 0):
                            print("Error: no name given.")
                        else:
                            break
                    while (True):
                        age = input("New age: ")
                        if (len(age) == 0):
                            print("Error: no age given.")
                        elif (age.isnumeric() == False):
                            print ("Error: invalid age given.")
                        else:
                            break
                    signedInUser.editDetails(name, age)
                    print("\nDetails successfully changed.")

                #2b. Add a friend.
                elif (choice2 == "2"):
                    if (len(socialNetwork.personList) < 2):
                        print("\nError: no other registered accounts.")
                    else:
                        print("\nOther Accounts:")
                        for person in socialNetwork.personList:
                            if (person != signedInUser):
                                print(person.name)
                        print("")
                        while (True):
                            friendTarget = None
                            selectedName = input("Add who as a friend? ")
                            for person in socialNetwork.personList:
                                if (selectedName == person.name):
                                    friendTarget = person
                            if (friendTarget == None):
                                print("Error: invalid name given.")
                            else:
                                break
                        signedInUser.addFriend(friendTarget)
                        print("")
                        print(friendTarget.name, "has successfully been added as a friend.")

                #3b. View all my friends.
                elif (choice2 == "3"):
                    if (len(signedInUser.friendList) == 0):
                        print("\nError: no friends have been added.")
                    else:
                        print("\nFriends Added:")
                        for friend in signedInUser.friendList:
                            print(friend.name)

                #4b. Send message to friend.
                elif (choice2 == "4"):
                    if (len(signedInUser.friendList) == 0):
                        print("\nError: no friends have been added.")
                    else:
                        print("\nFriends Added:")
                        for friend in signedInUser.friendList:
                            print(friend.name)
                        while (True):
                            messageTarget = None
                            selectedName = input("Send message to: ")
                            for person in signedInUser.friendList:
                                if (selectedName == person.name):
                                    messageTarget = person
                            if (messageTarget == None):
                                print("Error: invalid name given.")
                            else:
                                break
                        while (True):
                            content = input("Message text: ")
                            if (len(content) == 0):
                                print("Error: no text given.")
                            else:
                                break
                        print("")
                        print(signedInUser.sendMessage(friendTarget, content))
                

                #5b. View all my messages.
                elif (choice2 == "5"):
                    if (len(signedInUser.messageList) == 0):
                        print("\nNo messages recieved.")
                    else:
                        print("\nMessages:")
                        for message in signedInUser.messageList:
                            print(message)

                #6b. Block another account.
                elif (choice2 == "6"):
                    if (len(socialNetwork.personList) < 2):
                        print("\nError: no other registered accounts.")
                    else:
                        print("\nOther Accounts:")
                        for person in socialNetwork.personList:
                            if (person != signedInUser):
                                print(person.name)
                        print("")
                        while (True):
                            blockTarget = None
                            selectedName = input("Who will be blocked? ")
                            for person in socialNetwork.personList:
                                if (selectedName == person.name):
                                    blockTarget = person
                            if (blockTarget == None):
                                print("Error: invalid name given.")
                            else:
                                break
                        signedInUser.blockPerson(blockTarget)
                        print("")
                        print(blockTarget.name, "has successfully been blocked.")

                #7b. Go back.
                elif (choice2 == "7"):
                    break

                #Otherb.
                else:
                    print("Error: invalid number given")

    #3a. Quit.
    elif (choice == "3"):
        socialNetwork.saveSocialMedia()
        print("\nHave a great day!")
        break

    #Othera.
    else:
        print("Error: invalid number given")
