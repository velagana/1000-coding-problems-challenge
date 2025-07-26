# Take choices from both players
player1 = input("Player 1: Enter Rock, Paper, or Scissors: ").lower()
player2 = input("Player 2: Enter Rock, Paper, or Scissors: ").lower()

# Check for draw
if player1 == player2:
    print("Draw")

# Player 1: Rock
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins")
    elif player2 == "paper":
        print("Player 1 loses")
    else:
        print("Invalid input from Player 2")

# Player 1: Paper
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins")
    elif player2 == "scissors":
        print("Player 1 loses")
    else:
        print("Invalid input from Player 2")

# Player 1: Scissors
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins")
    elif player2 == "rock":
        print("Player 1 loses")
    else:
        print("Invalid input from Player 2")

# Invalid input from Player 1
else:
    print("Invalid input from Player 1")
