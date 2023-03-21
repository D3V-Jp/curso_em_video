# CRIE UM PROGRAMA QUE LEIA NUMEROS INTEIROS E ENTREGA A SOMATORIA SOMENTE DAQUELES QUE SAO PAR
from time import sleep

inicio = int(input('Leitura se inicia no numero: '))
fim = int(input('Leitura finaliza no numero: '))
result = 0

for c in range(inicio,fim+1):
    if c%2 == 0:
        result += c
        print(result)
# Acabei aprendendo essa logica em outra lição que acabei fazendo. 01/03/23