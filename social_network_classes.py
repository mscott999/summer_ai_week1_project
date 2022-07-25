import json

#Class used to represent the entire network of individual profiles.
class SocialNetwork:
    def __init__(this):
        #List of registered users in the network.
        this.personList = [] 
        
    #Saves the state of the network locally.
    def saveSocialMedia(this):
        pass
    
    #Restores the state of the network from previous session.
    def reloadSocialMedia(this):
        pass

    #Registers a new account in the social network.
    def createAccount(this, person):
        this.personList.append(person)

#Class used to represent individual users in the network.
class Person:
    def __init__(this, name, age):
        this.name = name
        this.age = age
        this.friendList = []
        this.blockList = []
        this.messageList = []

    #Alters the user's details after registration.
    def editDetails(this, name, age):
        this.name = name
        this.age = age
    
    #Adds a registered user to friendList.
    def addFriend(this, person):
        this.friendList.append(person)
    
    #Adds a registered user to blockList.
    def blockPerson(this, person):
        this.blockList.append(person)
    
    #Adds a message to a registered user's messageList.
    def sendMessage(this, person, content):
        if this in person.blockList:
            return person.name + "has blocked you! The message cannot be sent."
        message = "{0}: {1}".format(this.name, content)
        person.messageList.append(message)
        return "Message successfully sent."