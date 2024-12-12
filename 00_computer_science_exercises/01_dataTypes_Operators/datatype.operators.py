






# Boolean - bool - True or False values.

# Float - float - any number valuse with a decimal, +/-, including 0.0

# Integers - int - any whole number, +/-, including 0.

# Data types are stored in VARIABLES.
# A variable is basically a bucket with a name to put data into.
# VARIABL NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN ITI
# VARIABLES CANNOT START WITH A NUMBER
# camelCaseVariableNames
#snake_case_variable_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 7859879 # int data type
highScore = 9320490 # int data types

carSpeed = 12.55 # float data type, miles per hour
car_speed = -1.2452340024 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

playerName = "Keyon walker" # string data type
enemyType = "fire" # string data type

# ASSIGN NEW VALUES
playerName = "Billy Smith"
carSpeed = -1.25

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 5.0

# Printing Data Types
newInt = 3 
newFloat = 4.0
newString = "Skibidi Toilet"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type)


# printing variables to console / Screen
print(playerName)
print(isPurple)
print(high_score)
print(car_speed)

# printing variables and expressions to console / screen
print(high_score + 5000)
















 myint = myInt + 5

myNum = myInt + myFloat
# When you add an int and a float together, the answer becomes a float

# substraction
myNum = myInt - myFloat
myInt = myFloat - 1.25

# Multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerator, second num is denominator

# MODULUS (MODULO) % -- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBERS.
numStudents = 6
numSlicesPizza = 35

left0vers = numSlicesPizza % numStudents
print(left0vers)

# EXPONENTS **
numSquared = 5 ** 2 # 5 is the base, 2 is the exponent

# FLOOR-DIVISION // -- Divides, throws out any decimal.
myNum = my int // myFloat

# Addiction-Assignment Operator - Mostly used for counters.
myNum = 5
myNum = myNum + 1 # Old-School Method
myNum += 1 # New Hotness
myNum *= 1
myNum /= 1

# COMPARISON OPERATORS

# IS-EQUAL-TO == Are the two values to each other?
# Returns True or False based on evaluation.\
x = 6
print(x == 5)

# NOT-EQUAL-TO != Are the two values NOT equal?
# Returns True or False bases on evaluation.
print(x != 12)

# GREATER THAN /  GREATER-THAN-OR-EQUAL TO
print(5 > 3) # Greater Than
print(12 >= 2) # Greater Than or Equal To

# LESS THAN / LESS-THAN-OR-EQUAL TO
print(5 < 3) # LESS Than
print(12 <= 2) # Less Than or Equal To

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATMENT TO BE TRUE
age = 17
height = 73.5
# In order to ride the Teacups,you must be at least 18 years old and at least 60" tall.
print(age >=18 and height >= 60)
print(age >= 18 and height >= 60 and eyeColor == "Black")
# IDENTITY OPERATORS
# ALWAYS CHECK FOR THE LEAST-LIKELY TO BE TRUE CONDITION FIRST!!
print(defeatedBoss == True and level > 5 and hasBlueKey == True)

# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
print(age >= 18 or height >= 60)
print(age >= 18 or height >= 60 or eyeColor == "Blue")
# ALWAYS CHECK FOR THE LEAST-LIKELY TO BE TRUE CONDITION FIRST!!
#print(defeatedBoss == False or level > 5 or hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT.
a = 5
print(a == 5)
print(not (not (a == 5)))

# COMBINING LOGICAL OPERATORS
print(a == 5 and hasKey == True or isCloud == True)
TRUE AND

# LOGICAL OPERATIONS

# IDENTITY OPERATORS
