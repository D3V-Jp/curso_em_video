r1 = int(input('Qual o tamanho da primeira reta?: '))
r2 = int(input('Qual o tamanho da segunda reta?: '))
r3 = int(input('Qual o tamanho da terceira reta?: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('É possivel sim formar um TRIANGULO com essas retas.')
    if r1 == r2 and r3 == r1:
        print('Você formou um triangulo EQUILATERO!')
    elif r1 == r2 != r3 or r3 == r1 != r2:
        print('Você formou um triangulo ISÓCELES!')
    else: print('Você formou um triangulo ESCALENO!')
else: print('Infelizmente não foi possivel formar seu TRIANGULO!')
#Lição gostosinha de se fazer, não achei muito dificil, mas devo ter feito de forma mais complicada. 25/02/23