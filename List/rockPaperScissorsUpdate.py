import random
wins = 0
draws = 0
losses = 0
spam = ['rock', 'paper', 'scissors'] # List of options to choose from
rock, paper, scissors = spam # multi-assignment operation/unpacking
player_mssg = 'Player Wins!'
cpu_mssg = 'CPU Wins!'
while True:
    print(f'wins: {wins}, draw: {draws}, losses: {losses}')
    while True:
        print('Enter rock, paper or scissors') # player choice
        player = input('>').strip().lower()
        if player not in spam:
            continue
        print(f'Player: {player}')
        break

    cpu = random.choice(spam) # computer choice
    print(f'CPU: {cpu}')

    if player == cpu:
        draws += 1
        print('A tie!')
    elif player == rock and cpu == scissors:
        wins += 1
        print(player_mssg)
    elif player == paper and cpu == rock:
        wins += 1
        print(player_mssg)
    elif player == scissors and cpu == paper:
        wins += 1
        print(player_mssg)
    else:
        losses += 1
        print(cpu_mssg)

