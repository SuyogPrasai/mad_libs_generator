# Simple mad libs generator in python 

import os

noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")

os.system("cls") # Clearing the screen 

message = f"roses are {adjective1},\n{noun1} are blue,\n{noun2} are {adjective2},\nAnd so are you!"
print(message)
