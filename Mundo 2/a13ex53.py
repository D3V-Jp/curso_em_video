frase1 = str(input('Digite uma frase para analise do palindromo: ')).strip().upper()
frase2 = frase1.split()
frase3 = ''.join(frase2)
frase_invertida = frase3[::-1]

if frase3 == frase_invertida:
    print('A palavra {} escrita ao contrario é {}, então logo é UM PALIDROMO!'.format(frase1,frase_invertida))
else: 
    print('A palavra {} escrita ao contrario é {}, portanto NÃO é um PALIDROMO!'.format(frase1,frase_invertida))
# Fiz uso de uma AI para solucionar, e ela me deu uma soluçao interessante na linha 4. 06/03/23