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

def conversorsaida(saida): #define método 
    saida = format(saida, '.2f') #formata para exibir 2 casas decimais
    saida = str(saida) #converte em string
    saida = saida.replace('.',',') #substitui . por ,
    return saida #retorna a variável modificada pelo método

print('Alerta! Instruções de uso\n 1- Use ponto como separador decimal\n 2- Não use separador de milhar')

try: #try - except traz erro de entrada caso a entrada fornecida não possa ser executada pelo bloco dentro do try
    valorconta = float(input('Informe o valor total de consumo: R$  '))
except:
    print('Valor inválido')
    exit()

try:
    numeropessoas = int(input('Informe o total de pessoas: ')) #captura entrada para a variável definindo que o tipo será inteiro
    if  numeropessoas <= 0 or not type(numeropessoas) == int: #Define que se a variável for <= zero ou não for do tipo inteira cairá na exceção abaixo
        raise Exception #cria exceção se o número estiver fora do intervalo 
except: #se valor invalido para inteiro ou fora do intervalo, executa abaixo
    print('Valor inválido')
    exit()

taxaservico = float(input('Informe o percentual do serviço entre 0 e 100: '))
if taxaservico < 0 or taxaservico > 100:
    print('Valor inválido')
    exit()

valortotal = round((((taxaservico/100)+1)*valorconta),2)

from math import floor #floor serve para arredondar para baixo
porpessoa = ((floor((valortotal/numeropessoas)*100)))/100 #gambiarra, como o floor só arredonda para inteiro multipliquei por 100 para tornar inteiras as casas decimais de interesse, usar floor e dividir 100 para retornar o numero só que arredondado
print(porpessoa)
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

    