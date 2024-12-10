#Sets são conjuntos, características de set:
#São mutáveis, mas aceitam apenas tipos imutáveis como valor interno. 
#São úteis para remover valores duplicados
#Não tem índexes
#Não garantem a ordem
#São iteráveis (for, in, not in)

novoset = set() #set aqui indica a classe, cria um set vazio

stringset = set('abcdef')
print(stringset) #a saída será elemento a elemento e não necessáriamente na ordem, algo como {'b','c'...}

criaset = {'elemento1',1,5,'elemento'}
print(criaset)

lista = ['ba','ba','lao']
lista2 = set(lista) #Retira os elementos repetidos
print(lista2)

print ('ba' in lista) #saída True, exemplo de iteração em set

#Alguns métodos úteis em set (add, update, clear, discard)
set1 = set()
set1.add(1) #adiciona o '1' em set1, aceita apenas um valor por vez
set1.update(('Oi',5,4)) #adiciona essa tupla dentro do set
print(set1)
set1.discard('Oi') #descarta o elemento 'Oi'
print(set1)

#Operadores úteis ('|' ou .union,'&' ou .intersection,'-'ou diference,'^') 
conjuntoA = {'A', 'B','C'}
conjuntoB = {'B','C','D'}

ABuniao = conjuntoA.union(conjuntoB) #Poderia ser ABuniao = conjuntoA | conjuntoB
print(ABuniao)

ABintersec = conjuntoA & conjuntoB #o que há de igual em ambos
print(ABintersec)

ABdifere = conjuntoA - conjuntoB
print(ABdifere)

ABsimdif = conjuntoA ^ conjuntoB #diferença simétrica, ou seja, o que só tem em A que não tenha em B