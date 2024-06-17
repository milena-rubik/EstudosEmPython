# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args): #uso '*args' para receber argumentos não nomeados
    total = 1 #inicio meu total em um
    for numero in args:
        total *= numero #equivale a 'total = total * numero'
    return total

testemultiplicar = multiplicar(3,6,9)
print(testemultiplicar)
