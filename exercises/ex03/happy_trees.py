"""Drawing forests in a loop."""

__author__ = "730407726"


# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
h: int = int(input("Depth:"))
i: int = h + 0
while i >= len(TREE):
    j: int = i + 0
    while j < len(TREE):
        print(TREE[j])
        j += 1
    i += 1