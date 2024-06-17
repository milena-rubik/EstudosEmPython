# Exercício
#Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro

#Minha solução
def duplicar(num):
    return num*2

def triplicar(num):
    return num*3

def quadruplicar(num):
    return num*4

print('O número 3 duplicado, triplicado e quadruplicado é:',duplicar(3),triplicar(3),quadruplicar(3)) #teste

#Otimização do professor (especialmente quando se precisa criar muitas funções parecidas e com mais linhas de comando do que o exemplo):
#Criar uma função que cria as funções
def cria_fdemultplicar(multiplicador):
    def multiplicar(numero):
        return numero*multiplicador
    return multiplicar

duplica = cria_fdemultplicar(2)
triplica = cria_fdemultplicar(3)
quadruplica = cria_fdemultplicar(4)

print('O número 2 duplicado, triplicado e quadruplicado é:',duplica(2),triplica(2),quadruplica(2)) #teste


