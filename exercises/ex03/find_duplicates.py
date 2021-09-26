"""Finding duplicate letters in a word."""

__author__ = "730407726"

word: str = input("Enter a word.")

i: int = 0
while i < len(word):
    j: int = i + 0
    while j < len(word):
        print(word[j])
        j += 1
    i += 1