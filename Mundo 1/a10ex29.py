import random
v = random.randint(76,100)
multa = (v-85)*7
print('... Sua velocidade foi registrada no radar')
if v >= 85:
    print("""Você estava à {} em um local que o maximo permitido era {}
    e por isso foi multado em um valor de {}R$""".format(v,'85',multa))
else: print('Você estava à {}, parabéns por tá abaixo do limite exigido.'.format(v))
# Mid diff. exigiu um pouco de processamento lógico. 08-07-2022