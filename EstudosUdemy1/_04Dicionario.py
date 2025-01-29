

from typing import KeysView #importa o tipo KeysView do módulo typing, serve para anotações de tipos, especialmente para funções que manipulam as visualizações de chaves de dicionários.


comida=dict(doce='bolo', salgado='pamonha') #cria dicionário, forma menos usada

#cria dicionário (forma mais usada):
festa = { 
    'data' : '24.06.2024',
    'tema' : 'junino',
    'endereço' : [
        {'rua': 'bandeirinhas', 'número':321}
    ],
    'valor' : 100.00

}

#Métodos úteis dos dicionários Python:
# len - mostra o número de chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

#EXEMPLOS:

print(len(festa)) #'len' mostra o número de chaves

print(festa.keys()) #keys fará retornar as chaves
print(list(festa.keys())) #retorna as chaves, mas em modo lista, podemos solicitar outros formatos como tupla

for chave in festa.keys(): #uma outra forma de se obter as chaves ou valores é com a iteração.
    print(chave)

print(list(festa.values())) #retorna os valores das chaves

print(list(festa.items())) #'items' retorna as chaves e seu respectivos valores

for chave, valor in festa.items(): #usando iteração para obter chave valor
    print(chave, valor)

festa.setdefault('numconvidados', 50) #50 será usado como padrão se 'nunconvidados' não for definido

# Se fosse feito festa1 = festa, festa estaria apontando para festa1 e suas modificações caso ocorram, é atualizado
#Já a cópia rasa - shallow copy - é de uma cópia e não atualiza, mas isso ocorre apenas com valores imutáveis, os de 'primeiro nível' (o que significa que se tiver
#dentro um valor mutável, 'mais níveis', como um outro dicionário ou lista, não vai ser copiado, mas sim linkado ou seja atualizado ligado ao original):
festa1 = festa.copy() #cópia rasa
festa1['tema'] = 'Mundo Bita' #altero apenas festa1, não impacta em nada 'festa' original
festa1['endereço'][0]['rua'] = 'dosanimais' #alteração em 'festa1' e 'festa' (lembrando que festa['endereço'] acessa a lista de endereços, [0] pega o primeiro dicionário dessa lista, ['rua'] acessa a chave 'rua' dentro do dicionário)
print(festa)
print(festa1)
#Para copiar os níveis, valores mutáveis, precisaria fazer uma 'deep' copy:
import copy #precisa importar copy
festa2 = copy.deepcopy(festa)

#get
print(festa.get('tema')) #get apresenta o valor de uma chave
print(festa.get('presente', 'não cadastrado')) #caso a chave não exista mostra o segundo termo

#pop
testepop = festa.pop('data') #rouba (porque deleta em festa) a chave 'data' e atribui o valor a 'testepop'
teste2pop = festa.popitem() #rouba o último item de 'festa' para 'teste2pop'
print(testepop)
print(teste2pop)
print(festa)

#update atualiza o valor no dicionário
festa.update({
    'tema': 'novo tema'
    })
print(festa)


#DICIONARIOS PARA PRÓXIMOS EXEMPLOS:

pessoa = {
    'nome': 'fulano',
    'sobrenome': 'das coves'
}

dados = {
    'escola': 'tia marcy',
    'serie': 'nivel 2'
}

# Unir dicionários
diciocompleto = {**pessoa, **dados} #cria um dicionário com as chaves e valores dos dicionários 'pessoa' e 'dados'
print(diciocompleto)


#Para criar função que recebe argumentos nomeados (ela cria tipo um dicionário) use o '**kwargs', lembrando que para argumentos não nomeados usamos apenas '*args':
def recebe_argumentos_nomeados(**kwargs):
   for chave, valor in kwargs.items():
    print(chave, valor)
    
recebe_argumentos_nomeados(teste = 'argumento nomeado', num=123)

#Poderia usar a função acima para desempacotar um dicionário existente, exemplo:

recebe_argumentos_nomeados(**diciocompleto) #saída será 'chave valor' de cada item

#Outras formas de desempacotamento de dicionário:

a, b = pessoa.values() #atribui o valor das chaves a 'a' e 'b'
print(a, b) #tem saída 'fulano das coves'

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2) #saída: 'nome fulano'
print(b1, b2) #saída 'sobrenome das coves'



