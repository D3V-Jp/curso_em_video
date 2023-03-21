import bisect

numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: {numbers}')
# Muito dificil peguei rsp do video. 18/03/23