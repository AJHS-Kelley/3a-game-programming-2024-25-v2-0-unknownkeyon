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




