# Rock, Paper, Scissors by Keyon Walker, v0.0

# MODULE IMPORTS
import random, time

# DATA STRUCTURES
playerScore = 0
playerName = "Test Player"
playerChoice = None


# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please type your name and press enter.\n")
print(f"Hello {playerName}!\n")
isCorrect = input("Is that correct?  Type yes or no and press enter.\n").lower()
# .lower() can turn ALL input into lowercase.
# .upper() can turn ALL input into UPPERCASE.

if isCorrect == "yes":
    print(f"Ok {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type your name and press enter.\n")

# THE RULES using MULTI-LINE STRINGS
print(f"""
Welcome, {keyon} to the Rock, Paper, Scissors Robot!
It's Time To Play Rock, Paper, Scissors!
      
You will play against the CPU.  The first player to score 5 points wins.
You will select from ROCK, PAPER, OR SCISSORS.
The CPU will select ROCK, PAPER, SCISSORS at random.

1) ROCK BEATS SCISSORS
2) SCISSORS BEATS PAPER
3) PAPER BEATS ROCK
""")s

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS




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
        playerScore += 1
    elif playerCHoice == "paper" and cpuChoice == "paper":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
    else:
        print("Unable to determine a winner. Please restart")
        exit()


print(f"Your Final Score: {playerScore}\nCPU Final Score: {cpuScore}\n")
if playerScore > cpuScore:
    print(f"Congratulations {playerName}, a winner is you!\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. You are a disappointment to all.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()

    




        







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