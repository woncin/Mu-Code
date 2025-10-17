
import random
guess = ''
tosses = {'heads' : 1, 'tails' : 0}
while guess not in tosses:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if tosses[guess] == toss:
    print('You got it!')
else:
    if toss == 1:
        print('Nope, it was heads.')
    else:
        print('Nope, it was tails.')

