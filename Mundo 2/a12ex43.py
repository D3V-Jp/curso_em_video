alt = float(input('Qual sua altura?: '))
peso = float(input('Qual seu peso?: '))
imc = peso / alt**2

print('{:.2f}'.format(imc))

if imc < 16:
	print("Magreza grave")
elif imc < 17:
	print("Magreza moderada")
elif imc < 18.5:
	print("Magreza leve")
elif imc < 25:
	print("Saudável")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II (severa)")
else:
	print("Obesidade Grau III (mórbida)")
#Tava facil mas peguei o codigo do google para facilitar. 25/02/23