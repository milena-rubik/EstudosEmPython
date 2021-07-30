#1-Crie um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.
#2- Mostre se o número é par ou impar
numero = float(input('Informe um número '))

if numero < 0:
    print('O número é negativo')
elif numero > 0:
    print('O número é positivo')
else:
    print('O número é zero')

if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')




