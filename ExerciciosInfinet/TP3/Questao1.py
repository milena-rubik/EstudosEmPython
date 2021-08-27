""" Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando o número de
 pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom. Ao usuário do programa serão solicitados o valor total do consumo,
 em reais, o número total de pessoas e o percentual do serviço prestado, entre 0 e 100.
Fluxo de exceção: 
O programa deve verificar se o número total de pessoas é maior do que zero.
O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.
Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), usando vírgula como separador de casa decimal, em vez de pontos.
Para isso, converta o valor final da conta em uma string, usando a função str() e, em seguida, substitua os pontos por vírgulas com replace('.',','). Exemplo:
valor = 1.99 # Valor numérico 
valor = str(valor) # Converte o valor para uma string
valor.replace('.', ',') # Substitui pontos por vírgulas
print(valor) # Imprimirá 1,99
Exemplo de saída do programa:
Informe o valor total do consumo: R$ 100.00
Informe o total de pessoas: 2
Informe o percentual do serviço, entre 0 e 100: 10
O valor total da conta, com a taxa de serviço, será de R$ 110,00.
Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$ 55,00. """ 

def conversorentrada(entrada): #função criada para permitir também o uso da vírgula como separador decimal
    entrada = entrada.replace(',','.')
    return entrada


def conversorsaida(saida): #define método 
    saida = format(saida, '.2f') #formata para exibir 2 casas decimais
    saida = str(saida) #converte em string
    saida = saida.replace('.',',') #substitui . por ,
    return saida #retorna a variável modificada pelo método

print('Alerta! Não use separador de milhar!')

try: #'try - except' executa o except caso a entrada fornecida não possa ser executada pelo bloco do try
    valorconta = input('Informe o valor total de consumo: R$  ')
    valorconta = float(conversorentrada(valorconta))
    if valorconta <0:
        raise Exception
except:
    print('Valor inválido')
    exit() #dá ordem para fechar o programa, como requisitado que ocorresse em caso de erro no enunciado da questão

try:
    numeropessoas = input('Informe o total de pessoas: ') #captura entrada para a variável definindo que o tipo será inteiro
    numeropessoas = int(conversorentrada(numeropessoas))
    if  numeropessoas <= 0 or not type(numeropessoas) == int: #Define que se a variável for <= zero ou não for do tipo inteira cairá na exceção abaixo
        raise Exception #gera exceção se não atender a condição acima
except: 
    print('Valor inválido')
    exit()

try:
    taxaservico = input('Informe o percentual do serviço entre 0 e 100: ')
    taxaservico = float(conversorentrada(taxaservico))
    if taxaservico < 0 or taxaservico > 100:
         raise Exception
except:
    print('Valor inválido')
    exit()

valortotal = round((((taxaservico/100)+1)*valorconta),2) #traz o valor total da conta incluíndo a taxa de serviço arredondado em 2 casas decimais

from math import floor #floor serve para arredondar para baixo
porpessoa = ((floor((valortotal/numeropessoas)*100)))/100 #como o floor só arredonda para n° inteiro e preciso de 2 casas decimais, multipliquei por 100 para tornar inteiras as casas decimais de interesse, usar floor e dividir 100 para retornar o numero só que arredondado
resto = round(valortotal - (porpessoa*numeropessoas),2) 
umapessoa = porpessoa + resto

valortotal = conversorsaida(valortotal)
porpessoa = conversorsaida(porpessoa)
umapessoa = conversorsaida(umapessoa)

print(f'O valor total da conta incluindo a taxa de serviço é R$ {valortotal}')

if resto == 0:
    print(f'Dividindo a conta por {numeropessoas} pessoa(s), cada pessoa deverá pagar R$ {porpessoa}')
else:
    print(f'Dividindo a conta por {numeropessoas} pessoa(s), uma pessoa deverá pagar R$ {umapessoa} e cada uma das demais pessoas R$ {porpessoa}')

#PARTE BÔNUS
if resto != 0: #Se resto diferente de zero
    listaparticipante = list()
    numeroparticipantes = int(input('Se você deseja que quem irá pagar o maior valor seja sorteado digite o número de participantes desse sorteio '))
    for x in range (1,numeroparticipantes + 1): #percorre o código abaixo no intervalo selecionado
        participante = input(f'Digite o nome do {x} participante ')
        listaparticipante.append(participante) #adiciona o nome digitado a posição 'x' em participante
    import random
    print(f'O Azarado a pagar a sua parte mais o restante da conta é {random.choice(listaparticipante)}')
else:
    print('Podem brigar!')
    exit()
