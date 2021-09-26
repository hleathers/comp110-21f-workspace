"""An exercise in remainders and boolean logic."""

__author__ = "730407726"


# Begin your solution here...
number: int = int(input("Type a number."))
if number % 2 == 0 and number % 7 == 0:
    print("TAR HEELS")
else:
    if number % 2 == 0:
        print("TAR")
    else: 
        if number % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")