nameUnf = str(input('Seu nome e sobrenome por favor > ')).strip()
name = nameUnf.title()
nameSplit = nameUnf.split()
space = '//'
print('Seu nome em maiscula é {}'.format(name.upper()))
print('Seu nome em minusculo é {}'.format(name.lower()))
print('Seu nome tem um total de {}números'.format(len(name.strip( )) - name.count(' ')))
print('Seu primeiro nome tem {}números'.format((len(nameSplit[0]))))
# Consegui fazer, menos a parte de printar quantos caracteres tem sem o espaço. 02-07-2022