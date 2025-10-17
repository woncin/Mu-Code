print('Enter a number:')
num = int(input('> '))  # convert directly to int

if num > 0:
    if num % 2 == 0:
        print('Positive and even')
    else:
        print('Positive and odd')
elif num < 0:
    if num % 2 == 0:
        print('Negative and even')
    else:
        print('Negative and odd')
else:
    print('Zero')

