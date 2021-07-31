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

#Versão menos trabalhosa que pensei depois

numeros = list()
for i in range (0,3): #executa o comando abaixo 3 vezes
 num = float(input('Digite um número ')) 
 numeros.append(num) # adiciona o num a lista

numeros = set(numeros) #transforma a lista em conjunto comando útil para remover duplicidade
maior = max(numeros) #adiciona o maior numero do conjunto a variavel 'maior'
print(f'O maior número é {maior}')
