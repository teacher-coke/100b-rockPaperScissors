#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""


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


if __name__ == "__main__":
    player = playerChoice()
    print(player)
