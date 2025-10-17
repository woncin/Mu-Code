print('Enter weather condition')
weather = input('>')

if weather == 'Raining':
    print('Take an umbrella')
elif weather == 'Sunny':
    print('Enter temperature')
    temperature = input('>')
    if temperature == 'Hot':
        print('Wear sunglasses')
    if temperature == 'Cool':
        print('Wear jacket')
