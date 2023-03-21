from datetime import date
from random import randint

date = date.today().year
totmaior = 0
totmenor = 0

for p in range(1,1000+1):
    nasc = randint(1923,2023)
    idade = date - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} de maior, e {} de menor.'.format(totmaior,totmenor))
# Achei util, provavelmente usarei essa analise futuramente ne. 06/03/23
