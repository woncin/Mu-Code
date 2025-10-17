while True:
    print("Rock, Paper or Scissors?")
    print("Player 1")
    player1 = input(">").strip().lower()
    print("Player 2")
    player2 = input(">").strip().lower()
    if player1 == player2:
        print("It's a tie")
    elif player1 == "rock" and player2 == "paper":
        print("Player2 wins!")
    elif player1 == "paper" and player2 == "scissors":
        print("Player2 wins!")
    elif player1 == "scissors" and player2 == "rock":
        print("Player2 wins!")
    else:
        print("Player 1 wins")
