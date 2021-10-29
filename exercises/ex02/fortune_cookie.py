"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730407726"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
x: int = randint(0, 2)
print("Your fortune cookie says...")
if x == 0:
    print("Your life will be happy and peaceful.")
if x == 1:
    print("You will be happy.")
if x == 2:
    print("You will have everything you ever dreamed of.")
    
print("Now go spread positive vibes!")

# Begin your solution here...