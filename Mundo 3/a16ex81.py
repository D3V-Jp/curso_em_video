number = []
while True:
    n1 = int(input('Type a number: '))
    number.append(n1)

    confirm = '.'
    while confirm not in 'YyNn':
        confirm = str(input('Do you want to continue [Y/N]: ')).strip()[0]

        if confirm in 'YyNn':
            if confirm in 'Nn':
                break
        else:
            print('Please, select a valid option!')
    if confirm in 'Nn':
        break

print('=-'*20)

print(number)
number_reverse = sorted(number, reverse=True)
validated_five = 5 in number


print(f'You typed {len(number)} elements\nThe values in reverse: {number_reverse}')
if validated_five: 
    print('this list has the number 5.')
else: print('this list does not include number 5.')
# Usei a AI para me ajudar. 18/03/23