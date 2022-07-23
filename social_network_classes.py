class SocialNetwork:
    def __init__(this):
        this.peopleList = [] 
        
    def save_social_media(this):
        pass

    def reload_social_media(this):
        pass

    def  create_account(this, person):
        this.peopleList.append(person)


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
        message = "{0}: {1}".format(this.name, content)
        person.messageList.append(message)
