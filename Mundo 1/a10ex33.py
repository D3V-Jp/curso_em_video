from time import sleep
sleep(1)
print('-=-'*20)
n1 = int(input('Qual o primeiro número > '))
n2 = int(input('Qual o segundo número > '))
n3 = int(input('Escolha o terceiro número > '))
print('-=-'*20)
print('PROCESSANDO..')
sleep(1)
print('PROCESSAMENTO 75%')
sleep(0.5)
print('PROCESSAMENTO 100% CONCLUIDO..')
sleep(0.5)
print('-=-'*20)
# verificar o menor número
menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3

# verificar o maior número
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

# verificar o intermediario
medio = n1
if n2>menor and n2<maior:
    medio = n2
if n3>menor and n3<maior:
    medio: n3

print('O manor número é {}, o médio {} e o maior {}'.format(menor,medio,maior))
print('-=-'*20)