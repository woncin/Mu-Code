def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
        return value
    else:
        value = 3 * number + 1
        print(value)
        return value

try:
    number = int(input('Enter number: '))
    if number <= 0:
        print('Zero or negative not allowed')
    else:
        while True:
            number = collatz(number)
            if number == 1:
                break
except ValueError:
    print('Ivalid Input: Integers only')

