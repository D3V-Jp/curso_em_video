import random

numeros_sorte = tuple(random.randint(0,10) for c in range(5))

print(f'Os numeros sorteados foram {numeros_sorte}\n O maior numero sorteado foi {max(numeros_sorte)}.')
print(f'O menor numero sorteado foi {min(numeros_sorte)}.')
# Usei AI para me ajudar na linha 3. 15/03/23