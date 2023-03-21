list = [ ]

for count in range(0,5):
    list.append(int(input(f'Digit the value for position {count}: ')))
print('-='*20)
print(f' you typed: {list}\n the highest value is {max(list)}\n and the lower value is {min(list)}. ')
print('-='*20)
# no difficulty. 17/03/23