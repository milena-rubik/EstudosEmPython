# Função lambda é uma função anônima de uma linha


lista = [
     {'nome': 'Fulano', 'sobrenome': 'das Neves'},
     {'nome': 'Maria', 'sobrenome': 'Silva'},
     {'nome': 'João', 'sobrenome': 'Pé de Feijão'},
     ]
     
lista2 = [
     {'nome': 'Marciano', 'sobrenome': 'Ovin'},
     {'nome': 'Maria', 'sobrenome': 'Fumaça'},
     {'nome': 'Alecrim', 'sobrenome': 'Dourado'},
     ]
     
#Para ordenar essa lista poderia fazer:

def ordena(item):  #define a função 'ordena', que recebe como argumento um item (no caso, um dicionário da lista)
    return item['sobrenome'] #retorna o valor associado a chave 'sobrenome'
    
lista.sort(key=ordena) #o método sort tem dois argumentos nomeados opcionais: key e reverse (especificar =True para ordem descendente)

for item in lista: #percorre cada item da lista, ou seja, cada dicionário
    print(item)
#O Python usa a tabela unicode para fazer a ordenação

print("\n")

#Fazendo a mesma coisa só que usando lambda:
lista2.sort(key=lambda item: item['sobrenome']) #observar a estrutura, não precisou o nome de função, insiro o argumento e logo após : o retorno

for item in lista2: #percorre cada item da lista, ou seja, cada dicionário
    print(item)
    

#Nota sobre lista.sort(comando) e sorted(lista, comando): sort altera a própria lista e sorted faz uma cópia rasa e altera essa cópia.
