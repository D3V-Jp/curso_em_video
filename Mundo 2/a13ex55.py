import random
list = []
for c in range(1,10+1):
    peso = round(random.uniform(28,180), 1)
    list += [peso]
print('O maior peso registrado foi de {}, enquanto o menor foi de {}.'.format(max(list),min(list)))
# Eu nao conseguiria resolver sozinho entao vi nos comentario do yt. 06/03/23