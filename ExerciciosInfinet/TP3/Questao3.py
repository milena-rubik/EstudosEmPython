# Questão 03
# Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, variando de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.
# Fluxo de exceção: 
# O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.

listaparticipante = list() 
listanota = list()

for x in range (1,4): #percorre o código abaixo no intervalo selecionado
    participante = input(f'Digite o nome do {x} participante ')
    listaparticipante.append(participante) #adiciona o nome digitado a posição 'x' em participante
    while True: #Executa enquanto for verdadeiro, como por padrão é verdadeiro, a intenção é ficar repetindo em caso de 
        #entrada inválida até que seja digitado entrada válida caindo no 'else' e 'while' seja interrompido pelo break
        nota = float(input(f'Digite a nota do {x} participante '))
        if nota <0 or nota > 10 or not type(nota) == float:
            print('Entrada inválida')
        else:
            listanota.append(nota)
            break


indicevencedor = listanota.index(max(listanota))
print('indice vencedor',indicevencedor)
maiornota = max(listanota)
print('maior nota', maiornota)









        


# if  listanota.count(maiornota) > 1:
#     print('Houve empate!')
# else:
#     print(f'O vencedor é {listaparticipante[indicevencedor]} com nota {listanota[indicevencedor]}')