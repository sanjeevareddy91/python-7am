# Conditional Statements: Statements which will be executed based on certain conditions..

a=23

# print(a,"is greaterthan 40")

# 3 Different syntaxies of conditional statements..
    # if statement
    # if-else statement
    # if-elif-else statement
    # 

# If statements: It will check the condition if it is satisfied statements inside that will be executed.   

# Syntax:
"""
if condition:
    statements
"""
# a=50
# if a>40:
#     print(a,"is greatertha 40")

# print(a,"is lessthan 40")


# Syntax:
"""
if condition:
    statements
else:
    statements
"""

# a=30
# if a>40:
#     print(a,"is greatertha 40")
# else:
#     print(a,"is lessthan 40")

# user-input: asking the user to provide the input at execution time..

# input() - method to perform userinput actions..

# a=int(input("Enter a value:")) # ''

# print(a)
# # type - will return the datatype of your value..
# print(type(a))
# if a>40:
#     print(a,"is greatertha 40")
# else:
#     print(a,"is lessthan 40")

# eval() - It will take the value as your declared datatype format..


# name = suresh

# a=eval(input("Enter a value:"))

# print(a)
# print(type(a))


# Syntax 
"""
if condition:
    statements
elif condition:
    statements
elif condition:
    statements
else:
    statements"""

# you can declare n no.of elif , but before elif , if has to be declared for sure...
# else is not mandatory for the declaration..

# percentage = float(input("Enter your percentage:"))

# if percentage >= 70:
#     print("You got distinction!")
# elif percentage>=60 and percentage<70:
#     print("You for first class")
# elif percentage>=50 and percentage<60:
#     print("You got second class!")
# else:
#     print("No qualified!")

# nested condition: Writing conditionals inside other conditionals.
"""
if condition:
    if condiiton:
        statements
    else:
        statements
else:
    sattemanets
"""
# actor_name = input("enter actor name:")
# movie_name = input("Enter movie name:")
# if actor_name == 'chiru':
#     if movie_name == 'Khaidi150':
#         print("I'm Waiting!!!!")
#     else:
#         print("Veera shankar reddy!!")
# elif actor_name == 'Balayya':
#     if movie_name == 'Legend':
#         print("Seatu kadu kada assembly gate kuda takanivvanu!!!")
#     else:
#         print("Dabidi debeda!!")
# else:
#     print("Else statement nadi itha aaaa kick aa veru abba!!!!")


# Task is ATM Transactions: