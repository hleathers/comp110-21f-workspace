"""Project game."""

__author__ = "730407726"

import random

number: int = int(input("Guess a number:"))
points: int = 0
named_constant: str = '\U0001F920'
player: str


def main() -> None:
    global points
    global player
    greet()
    guess()
    score()
    finish: bool = True
    while finish:
        finish = bool(input("Do you want to play again? True or False:"))
        if finish:
            guess()
            score()


def complete() -> None:
    print("Congratulations your score is", points, player)


def greet() -> None:
    global player
    player = input("What's your name?")
    print("Welcome to the Guess That Number game!Lets play a number game where you guess the number between 1 and 200", player)


def guess():
    value = random.randint(1, 200)
    global number
    global player
    global points
    while number < int(value):
        print(f"That is lower than the wanted number, {player}")
        points = points + 1
        number = int(input("Guess again:"))
    if number > value:
        print(f"That is greater than the wanted number, {player}")
        points = points + 1
        number = int(input("Guess again:"))
    else:
        print("That's correct", named_constant)
        points = points + 5
        score()
        play()


def score() -> None:
    view: bool = bool(input("Want to view your score? True or False:"))
    if view:
        print(points)
        complete()
    

def play() -> None:
    global points
    global player
    total: bool = bool(input("Want to end the game? Enter True or False"))
    if total: 
        score()
        print(f"You have complete the game your points are{ points, player}")
    

if __name__ == "__main__":
    main()