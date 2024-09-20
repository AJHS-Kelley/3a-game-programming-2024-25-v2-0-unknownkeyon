# Rock, Paper, Scissors by Keyon Walker, v0.0

# MODULE IMPORTS
import random

# DATA STRUCTURES
playerScore = 0
cpuScore = 0
playerChoice = None

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please type your name and press enter.\n")
print(f"Hello {playerName}!\n")
isCorrect = input("Is that correct?  Type yes or no and press enter.\n")

if isCorrect == "yes":
    print(f"Ok {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type your name and press enter.\n")

# THE RULES using MULTI-LINE STRINGS
print(""
Welcome, {keyon} to the Rock, Paper, Scissors Robot!
It's Time To Play Rock, Paper, Scissors!
      
You will play against the CPU.  The first player to score 5 points wins.
You will select from ROCK, PAPER, OR SCISSORS.
The CPU will select ROCK, PAPER, SCISSORS at random.

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
     print(f"{keyon} you have {3} points.\nThe CPU has {4} points.\n")
     playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
























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