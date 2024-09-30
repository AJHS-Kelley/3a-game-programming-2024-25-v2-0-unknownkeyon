# Rock, Paper, Scissors by Keyon Walker, v0.0

# MODULE IMPORTS
import random, time

# DATA STRUCTURES
playerScore = 0
cpuScore = 0
playerChoice = None
numDraws = 0

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None


print(""
Welcome, {keyon} to the Rock, Paper, Scissors Robot!
It's Time To Play Rock, Paper, Scissors!
      
You will play against the CPU.  The first player to score 5 points wins.
You will select from ROCK, PAPER, OR SCISSORS.
The CPU will select ROCK, PAPER, SCISSORS at random.

# MAIN GAME LOOP




        # let cpu selec choice at random.
        cpuChoice = random.randint(0, 2) # randomly select 0, 1, or 2.
        if cpuChoice == 0:
            cpuChoice = "rock"
        elif cpuChoice == 1:
            cpuChoice = "scissors"
        elif cpuChoice == 2:
            cpuChoice = "paper"
        else:
            print("Unable to determine CPU choice.\nPlease restart.\n")
            exit()
         # print(f"CPU Choice: {cpuChoice}")
            
        # compare player choise to cpu choice
        if playerChoice == "rock" and cpuChoice == "paper":
            # CPU WINS
            print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
            print("the CPU wins a point.\n")
        


        # print the results to the screen
        # award point to winner and output
    elif cpuChoice == 2:
        cpuChoice = "paper"
    else:
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit()
    # print(f"CPU Choice: {cpuChoice}")

    # compare player choice to cpu choice
    if playerChoice =="rock" and cpuChoice == "paper":
        # CPU WINS
        print(f"The CPU chose {cpuCHoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
    elif playerChoice == "rock" and cpuChoice == "scissors":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "rock" and cpuChoice == "rock":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
    elif playerChoice == "scissors" and cpuChoice == "paper"
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
    elif playerChoice == "paper" and cpuChoice == "rock":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")


        







    loopCount += 1
    rpsTimeStop = time.time()
    rpsTime = rpsTimeStop - rpsTimeStart















# let cpu select choice at random.
cpuChoice = random.randint(0, 2) # randomly select 0, 1, or 2.
if cpuChoice == 0:
    cpuChoice = "rock"\
elif cpuChoice == 1:
    cpuChoice = "scissors"
elif cpuChoice == 2:
    cpuChoice = "paper"
else:
    print("Unable to determine CPU choice.\nPlease restart.\n")
    exit()


# compare player choice to cpu choice
if playerChoice == "rock" and cpuChoice == "paper":
print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
print("The CPU wins a point.\n")
cpuScore += 1
# CPU 