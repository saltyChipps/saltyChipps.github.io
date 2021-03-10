import time 
import random

room1visit = False
room2visit = False
room3visit = False
room4visit = False
room5visit = False

knifepresent = True
ducktapepresent = True
pistolpresent = True

def showItems():
    print ("you have:")
    if knifepresent == False: 
        print ("a knife")
    if ducktapepresent == False:
        print ("a roll of ducktape")
    if pistolpresent == False:
        print ("a pistol")

def intro(): # indents were messed up and there were no parenthesis
    print ("welcome to the adventure game.")
    playing=input("are you ready to start Y/N ")
    if playing == "y":
        print ("starting the game")
        print ("Type a number for each command (e.g. action=1) if you want to perform an action you type the corresponding number. ")
        print ("Your commands are as follows:  next room=1, previous room=2, use=3, take=4, and fight=5.")
        print ("If you need to remember the commands type 6 and they will pop up.")
        print ("Not all the commands will be possible at all times. If none of the commands do anything you might have missed something and need to go back. ")

# what are you trying to do?
# def ("room1")
#     else:
#         print ("thats too bad see you later")

def room1():
    if room1visit == False:
        print ('laurnn ipsum')
    room1visit = True
    r1 = input ("whatcha gonna do") # no colon here
    if r1 == "1":
        print ("you walk through the large door into a kitchen")
        def room2()
    elif r1 == "2":
        print (" there is no room to go back into")
    elif r1 == "3":
        print ("you can use things in the room you can also use thing that you are holding")
        print ("this room has a lamp")
        showItems()
        u1 = input ("\nwhat would you like to use ")
        if u1 == "knife" and knifepresent == False:
             print ("there is no reason to use this now")
        elif u1 == "ducktape" and ducktapepresent == False:
             print ("there is no reason to use this now")
        elif u1 == "pistol" and pistolpresent == False:
            print ("there is no reason to use this now")
        elif u1 == "lamp": 
            print ("you switch the lamp on it stays on for a few seconds only to flicker off")
        else: # needs an enter and colon
            print ("\nthat item doesnt exist or you dont have it")

    elif r1 == "4":
        print ("there is nothing here for you to take")
    elif r1 == "5":
        print ("there is nothing here for you to attack")
    elif r1 == "6":
        print ("Your commands are as follows:  next room=1, previous room=2, use=3, take=4, and fight=5.")
        print ("If you need to remember the commands type 6 and they will pop up.")
    else:
        print ("sorry thats not a valid command")


    print ("")
    #You wake up in a dimly lit room. You are sitting in a chair in the middle of the room.
    #  The last thing you remember was someone breaking into your house and kidnapping you.
    #  Now you need to escape. This room is elegantly decorated with velvet chairs and a fancy wall paper.
    #  It gives you a haunted manor vibe. There is a small table beside you with a lamp on it. The wall paper depicts red flowers in a green field.
    #  There is a large red rug on the floor containing a volcano. A large door swings open on of the walls. 
def room2
    if room2visit == False:
        print ("fhkjhdfkjahsldkjfhl")
        #add flavor stuff
    r2 = input ("what are u gonna du") # no colon
    if r1 == "2": # shouldn't be using an elif statement here
        print ("you walk back into the room you woke up in")
         def room1()
    elif r1 == "3":
        print ("you can use things in the room you can also use thing that you are holding")
        print ("this room has a set of cabniets and an oven ")
        showItems()
        u1 = input ("\nwhat would you like to use ")
        if u1 == "knife" and knifepresent == False:
             print ("there is no reason to use this now")
        elif u1 == "ducktape" and ducktapepresent == False:
             print ("there is no reason to use this now")
        elif u1 == "pistol" and pistolpresent == False:
            print ("there is no reason to use this now")
        elif u1 == "": 
            print ("")
        else print ("\nthat item doesnt exist or you dont have it")
    elif r1 == "4":
        print ("there is nothing here for you to take")
    elif r1 == "5":
        print ("there is nothing here for you to attack")
    elif r1 == "6":
        print ("Your commands are as follows:  next room=1, previous room=2, use=3, take=4, and fight=5.")
        print ("If you need to remember the commands type 6 and they will pop up.")
    # else: else what?


# incorrectly called all functions
room3()
room4()
room5()
conclusion ()