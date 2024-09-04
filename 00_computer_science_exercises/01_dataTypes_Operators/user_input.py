# User Input Practice, Keyon Walker, v0.0

# input () is the built-in funtion to get informaion from the KEYBOARD.
# BASIC EXAMPLE
variableName = input("Please type a variable name and press enter.\n")
print(variableName)

# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!

# INCORRECT, CAUSES A  CONCATENATION ERROR.
# myNumber = input("Please type an INTEGER number and press enter.\n")
# print(myNumber + 5)

# CORRECT -- Use a wrapper.
myNumber = int(input("Please type an INTEGER number and press enter.\n"))
print(myNumber + 5)

# Wrapper Functions
# int() will convert the data to an INTEGER if possible
# float() will convert the data to a FLOAT if possible
# str() will convert the data to a STRING if possible
# print(float(newNumber))