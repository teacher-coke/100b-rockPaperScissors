#!python3
from random import randint

"""rock     : 0
  paper    : 1
  scissors : 2"""


def player(c):
    if c == "rock":
        return 0
    elif c == "paper":
        return 1
    elif c == "scissors":
        return 2


def playerChoice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    return player(choice)


def computerChoice():
    option = int(randint(0, 2))
    return option


def playerWins(computer, player):
    if computer == 0 and player == 1:
        return 1
    elif computer == 0 and player == 2:
        return -1
    elif computer == 0 and player == 0:
        return 0
    if computer == 1 and player == 1:
        return 0
    elif computer == 1 and player == 2:
        return 1
    elif computer == 1 and player == 0:
        return -1
    if computer == 2 and player == 1:
        return -1
    elif computer == 2 and player == 2:
        return 0
    elif computer == 2 and player == 0:
        return 1


for i in range(5):
    p = playerChoice()
    c = computerChoice()
    if playerWins(p, c) == 0:
        print("Draw!")
    elif playerWins(p, c) == 1:
        print("You Won!")
    elif playerWins(p, c) == -1:
        print("You Lost!")

if __name__ == "__main__":
    pass
