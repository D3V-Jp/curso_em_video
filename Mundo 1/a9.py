n1 = 'Langue of death'
print('-'*30)
print(n1)
print(n1[::1])
print('_'.join(n1))
print(n1.split())
print("""Esse metodo de tres aspas é feito para printar um texto
muito longo de diversas linhas. ex: Finge que aqui tem um texto muito
longo.""")
print('-'*30)
print('Langue' in n1)

n1 = n1.replace('Langue','Batman')
print(n1,' // ', 'Langue' in n1 )

print(n1.find('batman'),' // ',n1.lower().find('batman'))