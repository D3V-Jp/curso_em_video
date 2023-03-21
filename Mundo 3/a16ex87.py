# variable of 'matriz'.
matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]

# format the 'matriz'.
for linha in range(0,3):
    for colun in range(0,3):
        matriz[linha][colun] = int(input('Number '))
print('=-'*20)

# print the 'matriz'.
for c in matriz:
    print(c)
print('=-'*20)

# calculate the even numbers.
even = []
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            even.append(elemento)
sum_even = sum(even)

# sum of third column.
third_column = 0
for linha in matriz:
    third_column += linha[2]

# second line highest value.
highest = max(matriz[1])

# print all results.
print('The sum of values even is', sum_even)
print('The sum of third column is', third_column)
print('The highest value in second line is', highest)
print('=-'*20)
# high difficulty for me. 20/03/23