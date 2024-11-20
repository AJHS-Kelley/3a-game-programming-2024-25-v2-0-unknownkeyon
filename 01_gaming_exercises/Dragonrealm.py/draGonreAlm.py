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
    print('A large dragon jumps out in front of you and starts chasing you')
    print("You are running...")

    print("would you like to pick up a banana slip?")
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



def path.Swamp(hasTorch: book) hoat:
alive = True
print("As the sun crests the sky to the east, you gather your gear and head north to the swamp.\n")
tine.strep(waitTime)
print("After a days journey along the Old King's Road, you stand on the outskirts of the swamps, \nYou spot a small clearing in the scrub and brush. It looks like a good place to camp.\n")
time.sleep(waitTime)
camp = input("Do you want to camp for the night?\n Enter yes or no then press enter. \n").lower()
If camp = "yes" and hasTorch:
print("As the sun sets and you prepare to camp, you take the small torch from your pack and light it.\n")
print("The flickering fire of the torch reveals...something...in the murky swamp waters creeping towards you. \n")
47
time.sleep(weitrime)
49
Lime.sleep(waitTime)
50
print("You scream loudly, waving the torch at the figure hidden in the swamps!\n")
31
time.sleep(waitTime)
print("You hear a high-pitched squeal as the hidden figure turns and runs, the splashing of muddy swamp water grows faint. An")
time.sleep(waitTime)
print("Whatever it was, is gone. You gather some fallen branches and logs to build a fire using the torch.\n")
time.sleep(waittine)
print("With a fire roaring, you feel sale from the dangers of the swamp. You sleep with one eye open, but manage to get some rest through the night. \n")
elif camp "yes" and not has Torch:
print("As the sun sets on the swamelands, darkness surrounds you. You really wish you had a torch right now...\n")
Lime,sleep(waitTime)
time.sleep(waitlime)
59
print("The swamp seens to come alive at night. You recognize the sounds of owls hooting, frogs croaking, and insects buzzing...")
61
62
print("Other sounds though, are not as familiar. Strange howls and grunts begin to echo through the gnarled trees of the swamp...")
time.sleep(waitlime)
print("The distinct sounds of footsteps splashing through the muddy water start to grow louder...\n")
time.sleep(waitTime)
print("The sounds of footsteps echo in your ear and now you can smell the distinct odor of goblins on the air...")
Line.sleep(unitTime)
print("Everything goes silent for a moment and then the grunts and howls of goblins echo as they burst forth from the darkness!")
Fine.sleep(waitTime)
print("The goblins jump on you, clawing and biting as you struggle to survive. You are still alive when they begin to eat you...\n")
alive = False
return ali
else:
print("You decide against camping in the swamps and press on through the night...")
time.sleep(waitTime)
print("As you march through the night, the swamp seems to come alive with noise. Owls, Frogs, and Insects fill your ears with their song...")
time.sleep(woitTime)
print("But you also hear other...things.. grunting and howling in the night. You wonder if they know you're here...")
time.sleep(waitTime)
if
random.randint(1, 2)-11
print("You creep slowly through the swamp, carefully checking for logs that may cause you to stumble...")
time.sleep(waitTime)
print("The sounds of the swamp creatures drass closer, but thankfully you are able to escape undetected. ") else :
print("You stumble over an unseen log in the water, creating a loud a splash, Your presences is definitely known to whatever is out there...\n")