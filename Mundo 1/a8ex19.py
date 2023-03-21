import random
n1 = str(input('Nome do aluno > '))
n2 = str(input('Nome do aluno > '))
n3 = str(input('Nome do aluno > '))
n4 = str(input('Nome do aluno > '))
lista = [n1,n2,n3,n4]
escolhido = random.choices(lista)
print('O aluno sorteado foi o: {}'.format(escolhido))
# Eu precisei de ajuda na linha 6 em diante. 28-06-2022