#Como fazer a mesma coisa que o método contar com uma função anônima
# utilizando uma linha. O 'lambida' informa que é função anonimaS
#erve para resolver coisas mais curtas para não precisar criar um método.

contadorcaracter = lambda lista: [len(x) for x in lista] 

if __name__ == '__main__':
    listadoce = ['jujuba', 'brigadeiro', 'chocolate']
    print(contadorcaracter(listadoce))

reajuste = lambda contrato, indice: round((contrato * indice),2) #round serve para manter a duas casas decimais

if __name__ == '__main__':
    print(reajuste(7607,0.0975)) 