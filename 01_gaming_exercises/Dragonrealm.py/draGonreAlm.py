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
# "a" CREATES FILE, IF FILE EXISTS, ERASE AND OVERWRITE FILE CONTENTS
# "a" CREATES FILE, IF FILE EXISTS, APPEND DATA TO THE FILE.          

saveData.write("GAME STARTED" + " " + str(datetime.datetime.now()) + "\n")                    

def displayIntro():

    print('You are in a village full of dragons. Right Infront of you,')
    print('you see 2 caves. In 1 cave, the dragon is friendly and wont harm you')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print('it is your job to pick the right cave to find the treasure.')
    print()
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You walk inside the cave...')
    time.sleep(2)
    print('It is very  dark and scary...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and eats you whole')
    print("")
    time.sleep(2)

    friendlyCave = random.randint(1, 2)


    if friendlyCave == 1:
        print('Gives you his treasure!')
    elif friendlyCave == 2:
        print('You lost!')
    elif friendlyCave == 3:
        print("You got destroyed")



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


