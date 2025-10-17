secret_number = 12
print('Guess the number')
num = int(input('>'))
if num == secret_number:
    print('Correct!')
elif num > secret_number:
    print('Too high')
else:
    print('Too low')
