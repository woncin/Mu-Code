print('Enter a number')
number = int(input('>'))
if number > 0:
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')
elif number < 0:
    print('Negative')
else:
    print('Zero')
