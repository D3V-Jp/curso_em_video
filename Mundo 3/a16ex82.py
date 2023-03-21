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

even = [ ]
odd = [ ]

for num in number:
    if num % 2 == 0:
        even.append(num)
    else: odd.append(num)

print("=-" * 20)
print("Here's what you typed:")
print(number)
print("Here are the even numbers:")
print(even)
print("Here are the odd numbers:")
print(odd)
# Facil ate. 18/03/23
