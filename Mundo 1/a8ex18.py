import random

ca = int(input('Cateto adjacente > '))
co = int(input('Cateto oposto > '))
h = ca+co
print('Cateto Adjacente = {}**2, Cateto Oposto = {}**2, Hipótenusa = {}**2'
.format(ca,co,h))
sena = co/h
cosa = ca/h
tga = co/ca
print('O seno é {:.3f}, Cosseno {:.3f}, Tangente {:.3f}'.format(sena,cosa,tga))
# Desafio 18 , acho que errei nos calculos, 28-06-2022
# Obs; eu esqueci de salvar os exercicio antigo, mas o primeiro foi +- 26-06-2022