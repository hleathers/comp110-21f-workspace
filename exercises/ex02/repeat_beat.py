"""Repeating a beat in a loop."""
__author__ = "730407726"

# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it?"))

if repeat <= 0:
    print("No beat...")
else:
    print((" " + beat) * repeat)