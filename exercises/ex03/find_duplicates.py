"""Finding duplicate letters in a word."""

__author__ = "730407726"

word: str = input("Enter a word: ")

i: int = 0
f: bool = False
while i < len(word):
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            f = True
        j += 1
    i += 1

print("Found duplicate: " + str(f))