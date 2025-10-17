birthdays = {'Alice': 'Apr 1',
             'Bob': 'Dec 12',
             'Carol': 'Mar 4'}
while True:
    print('Enter name: (OR press enter to quit)')
    name = input('')
    if not name:
        break
    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f'No information about {name}')
        bday = input('What is their birthday: ')
        birthdays[name] = bday
        print('Birthday database updated successfully')

