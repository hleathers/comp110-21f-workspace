"""List utility functions."""

__author__ = "730407726"


# TODO: Implement your functions here.

def dup(xs: list[int]) -> None:
    """Duplicate a list value."""
    start_len: int = len(xs)
    i: int = 0
    while i < start_len:
        xs.append(xs[i])
        i += 1
        print("False")
        if i > start_len:
            print("True")


nums: list[int] = [10, 20]
dup(nums)
print(nums)

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint)(1,6))

print(rolls)