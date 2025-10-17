tries_left = 5
secret_number = 12

while True:
    print('Enter a number')
    number = int(input('>'))
    if number != secret_number:
        if tries_left >= 0:
            tries_left -= 1
            if bool(tries_left):
                print(f'You have {tries_left} chance left ')
            else:
                print('Game over! Try again')
                break
    else:
        print('Congrats!')
        break

