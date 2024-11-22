# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
import datetime

# SAVING DATA TO A FILE
# STEP 1 -- Create the file name to use.
logFileName = "dragonRealmLog" + str(time.time()) + ".txt"
# Example: dragonRealmLog1132AM.txt

# STEP 2 -- Create / Open the file to save the data.
saveData = open(logFileName, "a")     
# FILE MODES
# "x" CREATES FILE, IF FILE EXISTS, EXIT WITH ERRROR MESSAGE.
# "w" CREATES FILE, IF FILE EXISTS, ERASE AND OVERWRITE FILE CONTENTS
# "a" CREATES FILE, IF FILE EXISTS, APPEND DATA TO THE FILE.          

saveData.write("GAME STARTED" + " " + str(datetime.datetime.now()) + "\n")         

hasSword = False
hasShield = False

items = 0
alive = True

def displayIntro():
    print('You are lost in the forest and you need somewhere to stay...')
    time.sleep(waitTime)
    print("There's some different camps you can try to stay at for the night...")
    time.sleep(waitTime)
    print("However beware, the residents might not be so welcoming...")

def chooseCamp() -> int:
    camp = ''
    while camp != '1' and camp != '2':
        print('Which camp will you go to? (1 for the Bandit Camp or 2 for the Archer Camp)')
        camp = input()
    print("CRASH POINT 1")
    return camp

def campScenario(camp, hasSword, hasShield):
    print("CRASH POINT 2")
    if camp == '1' and hasSword:
        print("You wander into the Bandit Camp, it doesn't look that big... there's barely any people.")
        time.sleep(waitTime)
        print("They don't seem to like you very much.")
        time.sleep(waitTime)
        print("They draw their weapons against you!")
        time.sleep(waitTime)
        print("You fend everybody off with your masterful sword skills, good thing you had it.")
        time.sleep(waitTime)
        print("The smell of the bodies is strong but you can finally get some sleep in one of the beds.")
    elif camp == '1' and hasShield:
        print("You wander into the Bandit Camp, it doesn't look that big... there's barely any people.")
        time.sleep(waitTime)
        print("They don't seem to like you very much.")
        time.sleep(waitTime)
        print("They draw their weapons against you!")
        time.sleep(waitTime)
        print("You block their strikes with your shield.")
        time.sleep(waitTime)
        print("One of them snuck up from behind and stabbed you!")
        time.sleep(waitTime)
        print("You passed out and died from bleeding out.")
        alive = False
        return alive
    elif camp == '2' and hasShield:
        print("You wander into the Archer Camp, it looks very intense.")
        time.sleep(waitTime)
        print("The leader of the camp greets you with a stoic look.")
        time.sleep(waitTime)
        print("He tells you that in order to stay at his camp, your reflexes must be tested.")
        time.sleep(waitTime)
        print("His archers aim their bows at you, prepare yourself.")
        time.sleep(waitTime)
        print("You block all the arrows with your shield with perfect movements.")
        time.sleep(waitTime)
        print("The leader tells you that you have earned his respect and earned a tent.")
        time.sleep(waitTime)
        print("Time to get some sleep.")
    elif camp == '2' and hasSword:
        print("You wander into the Archer Camp, it looks very intense.")
        time.sleep(waitTime)
        print("The leader of the camp greets you with a stoic look.")
        time.sleep(waitTime)
        print("He tells you that in order to stay at his camp, your reflexes must be tested.")
        time.sleep(waitTime)
        print("His archers aim their bows at you, prepare yourself.")
        time.sleep(waitTime)
        print("You manage to block two arrows with your sword before being overwhelmed with their attacks.")
        time.sleep(waitTime)
        print("The arrows were too much for you and your sword, you died.")
        alive = False
        return alive
    print("CRASH POINT 3")


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    waitTime = int(input("Please input how many seconds you would like the text to wait. Enter 1 - 3.\n"))
    displayIntro()
    print("Please select your weapon, 1 for Sword, 2 for Shield")
    weapon = input().lower
    if weapon == '1':
        hasSword = True
    elif weapon == '2':
        hasShield = True
    campNumber = chooseCamp()
    campScenario(campNumber, hasSword, hasShield)
    print('Do you want to play again? (yes or no)')
    playAgain = input()
