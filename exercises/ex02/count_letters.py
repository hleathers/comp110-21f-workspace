"""Counting letters in a string."""

__author__ = "730407726"


# Begin your solution here...
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
count: int = 0
i: int = 0

while i < len(word):
    if letter == word[i]:
        count += 1
    i += 1
print("Count: " + str(count))
