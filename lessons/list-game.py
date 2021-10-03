"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
        rolls.append(randint(1, 6))


# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# Access an individual item
print(rolls[0])
print(rolls[1])


# Access the length of a list (number of items)
print(len(rolls))

# Access the last item of a list
last_index: int = len(rolls) - 1
print(rolls[last_index])


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
    print(rolls)


def odds(min: int, max: int) -> list[int]:
    """Construct list of oddws, inclusive."""
    xs: list[int] = list()
    i: int = (min // 2) * 2 + 1
    while i <= max:
        xs.append(i)
        i += 2
    return xs


ys: list[int] = odds(3, 6)
print(ys)