import random
n1 = str(input('Nome do aluno > '))
n2 = str(input('Nome do aluno > '))
n3 = str(input('Nome do aluno > '))
n4 = str(input('Nome do aluno > '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
# Precisei de ajuda da linha 7 pra cima. 28-06-2022