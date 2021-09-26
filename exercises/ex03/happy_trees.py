"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
i: int = 0
while i < len(TREE):
    j: int = i + 0
    while j < len(TREE):
        print(TREE[j])
        j += 1
    i += 1