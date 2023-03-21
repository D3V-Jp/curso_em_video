m1 = float(input('Qual foi a média atingida na primeira matéria?: '))
m2 = float(input('Qual foi a média atingida na segunda matéria?: '))
med = (m1+m2) / 2
print(med)

if med <= 6.9 and med >= 5 :
    print('Infelizmente sua média foi de {} portanto você ficará para recuperação.'.format(med))
elif med >= 7:
    print('Felizmente sua média foi de {} por tanto você foi APROVADO!'.format(med))
elif med <= 5:
    print('Infelizmente sua média foi de {} por tanto você foi REPROVADO!'.format(med))

#Achei simples que nem a ultima, consegui usar o AND para diferencia do OR na hora de ler que a media
# é menor que 5. 24/02/23