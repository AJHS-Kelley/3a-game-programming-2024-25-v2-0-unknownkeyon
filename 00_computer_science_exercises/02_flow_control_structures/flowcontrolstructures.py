# Flow Control Structures, Keyon Walker, v0.0
# Making Computer Programs Make Decisions

temperature = 100.35
color = "Blue" 
height = 6
likesPineappleOnPizza = True

# SINGLE DECISION POINT - if statement
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of the time.
    # runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
    print("It is hot as the sun outside.\n")

if height < 6:
    print("No thanks, I have a boyfriend.\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineappleOnPizza:
    print("Yummy")

# What is we want something different to happen?
if color == "Red": # COMMON ERROR FOR STUDENTS IS USING = instead of ==.
    print("Your shirt is the correct uniform color.\n")
else:
    print("Your shirt is not the correct uniform color.\n")