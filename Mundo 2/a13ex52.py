n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)
# Peguei do google, mas achei mt inteligente o sistema de chavinha usado no Mult, lembro que ja tinha essa logica no curso de roblox. 02/03/23
