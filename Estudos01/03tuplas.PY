#TUPLA
#Principal diferença entre lista e tupla é que esta é imutável.

alimentot = ('pizza', 'hamburgão', 'churrasco') #declaro tupla usando () e não [] como na lista 
# 'alimento [1] = salada' retornaria um erro
print(len(alimentot)) #retorna n° de elementos numa lista ou tupla

lista = [3, 5, 7, 10, 11]
resultado = []
for x in lista:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)