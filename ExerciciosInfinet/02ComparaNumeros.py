#1-Crie um algoritmo que leia três números e mostre o maior número.
#Considere a entrada de números iguais, para um problema mais difícil.
#2- Mostre-os em ordem crescente.

num1 = float(input('Digite o primeiro número '))
num2 = float(input('Digite o segundo número '))
num3 = float(input('Digite o terceiro número '))


if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior número é {num3}')
elif num1 == num2 and num1 < num3:
    print(f'O maior número é {num3}')
elif num1 == num2 == num3:
    print(f'O maior número é {num1}')
elif num1 == num2 and num1 > num3:
    print(f'O maior número é {num1}')
elif num1 == num2 and num1 < num3:
    print(f'O maior número é {num3}')
elif num1 == num3 and num1 > num2:
    print(f'O maior número é {num1}')
elif num1 == num3 and num1 < num2:
    print(f'O maior número é {num2}')
elif num2 == num3 and num2 > num1:
    print(f'O maior número é {num2}')
elif num2 == num3 and num2 < num3:
    print(f'O maior número é {num3}')