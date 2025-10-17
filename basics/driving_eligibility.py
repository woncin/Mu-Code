print('Enter age')
age = int(input('>'))

if age >= 18:
    print('Do you have a divers license? Y/N')
    driver_license = input('>').upper()
    if driver_license == 'Y':
        print('You can drive')
    else:
        print('You need license')
else:
    print('Too young to drive')
