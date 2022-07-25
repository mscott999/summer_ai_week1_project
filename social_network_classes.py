import json

class SocialNetwork:
    def __init__(this):
        this.personList = [] 
        
    def saveSocialMedia(this):
        pass
    
    def reloadSocialMedia(this):
        pass

    def createAccount(this, person):
        this.personList.append(person)

class Person:
    def __init__(this, name, age):
        this.name = name
        this.age = age
        this.friendList = []
        this.blockList = []
        this.messageList = []

    def editDetails(this, name, age):
        this.name = name
        this.age = age
    
    def addFriend(this, person):
        this.friendList.append(person)
    
    def blockPerson(this, person):
        this.blockList.append(person)
    
    def sendMessage(this, person, content):
        if this in person.blockList:
            return person.name + "has blocked you! The message cannot be sent."
        message = "{0}: {1}".format(this.name, content)
        person.messageList.append(message)
        return "Message successfully sent."