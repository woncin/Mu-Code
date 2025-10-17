print('enter total bill')
bill = float(input('>'))
print('How many people')
no_of_persons = int(input('>'))
if no_of_persons <= 0:
    print('Invalid')
else:
    total = bill / no_of_persons
    print(f'{total:.2f}$ per person')
