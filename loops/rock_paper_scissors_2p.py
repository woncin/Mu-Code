print('ROCK, PAPER OR SCISSORS')
valid_moves = ('rock', 'paper', 'scissors')
while True:
    print('Player 1')
    player_1 = input('>')
    print('Player 2')
    player_2 = input('>')
    #  Check move validity
    if player_1 not in valid_moves or player_2 not in valid_moves:
        print('You must enter rock, paper or scissors')
        continue
    # Are both players inputs the same?
    if player_1 == player_2:
        print('It\'s a tie')
    #  Display winner
    elif player_1 == 'rock' and player_2 == 'scissors':
        print('Player1 wins')
    elif player_1 == 'paper' and player_2 == 'rock':
        print('Player1 Wins')
    elif player_1 == 'scissors' and player_2 == 'paper':
        print('Player1 wins')
    else:
        print('Player 2 wins')




