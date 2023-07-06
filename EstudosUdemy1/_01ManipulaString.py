nome = input('Digite o seu nome: ') #pede entrada e atribui a 'nome'
idade = input('Digite a sua idedade: ') 

if nome and idade: #Se o valor de ambas as variáveis forem true executará o bloco abaixo 
    print(f'Seu nome é {nome} e você tem {idade} anos')
    print(f'Seu nome invertido é {nome[::-1]}') #inverte a ordem de 'nome' [<start>:<stop>:<step>]
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} caracteres') #conta com os espaços
    print(f'A primeira letra do seu nome é {nome[0]} e a última é {nome[-1]}')#o índice invertido começa a contar do fim


else: #caso as variáveis não sejam preenchidas estarão vazias e corresponderão ao valor false
    print('Os dados não foram preenchidos')
    