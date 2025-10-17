balance = 10000
print('Enter withdrawal amount')
amount = int(input('>'))
if amount <= balance:
    if amount < 5000:
        print('Small withdrawal')
    else:
        print('Large withdrawal')
else:
    print('Insufficient fund')

