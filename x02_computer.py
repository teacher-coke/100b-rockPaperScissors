#!python3
from random import randint
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""


def computerChoice():
    option = int(randint(0, 3))
    return option


if __name__ == "__main__":
    computer = computerChoice()
    print(computer)
