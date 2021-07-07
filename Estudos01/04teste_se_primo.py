# verificar se o número é primo (números que são divisíveis apenas por 1 e ele mesmo, lembrando que 1 não é primo)

numteste = int(input('Entre com o número desejado'))
contdivisao = 0

for x in range (1, numteste+1): #numteste + 1 devido ao intervalo ser aberto
    resto = numteste % x
    if resto == 0:
            contdivisao += 1 #acrescenta 1 a cada resto de divisão que retorna 0
    
if contdivisao == 2: #2 porque primo é divisivel por 1 e ele mesmo
    print('número {} é primo'.format(numteste))
else:
    print('número {} não é primo'.format(numteste))