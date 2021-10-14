"""This is the numeric operator assignment."""
__author__ = "730407726"

leftside: int = int(input("Left-hand side: "))
rightside: int = int(input("Right-hand side: "))


print(leftside, "**", rightside, "is", leftside ** rightside)
print(leftside, "/", rightside, "is", leftside / rightside)
print(leftside, "//", rightside, "is", leftside // rightside)
print(leftside, "%", rightside, "is", leftside % rightside)