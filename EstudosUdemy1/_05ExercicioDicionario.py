
# Criar Sistema de perguntas e respostas usando dicionário

perguntas =[
    {
        'pergunta': 'Qual a princesa que comeu a maçã envenenada?',
        'opcoes': ['Branca de Neve', 'Cinderela', 'Ariel'],
        'resposta': 'Branca de Neve',
    },
        
    {
        'pergunta': 'Quem teve a casa assoprada por lobo?',
        'opcoes': ['Chapeuzinho Vermelho', 'Os três porquinhos', 'Pinóquio'],
        'resposta':'Os três porquinhos',
    }
    ]
acertos= 0 #para usar no placar

for cadapergunta in perguntas: #'cadapergunta' corresponde a cada dicionário da lista a ser percorrido perguntas[0],perguntas[1]...
    print(cadapergunta['pergunta'])
    
    for i, opcao in enumerate(cadapergunta['opcoes'], start=1): #o 'for i,'...'enumerate' enumera as opções, sem o start=1 começaria em zero
        print(f'{i}'+')', opcao)
        
     # Bloco de entrada e tratamento de erro    
    while True:  # Loop para garantir que o usuário insira um dado válido
        try:
            entrada = int(input('Insira o número da opção correta: '))
            if entrada < 1 or entrada > len(cadapergunta['opcoes']):
                print('Entrada inválida. Por favor, insira um número entre as opções.')
            else:
                break  # Entrada válida, sai do loop
        except ValueError:
            print('Entrada inválida. Por favor, insira um número válido.')
            
        
    if cadapergunta['opcoes'][entrada-1] == cadapergunta['resposta']: #índice da 'entrada' é ajustado com - 1, pois as listas em Python começam de zero.
        print('Parabéns, reposta certa!')
        acertos += 1 #incrementa 1 em acertos
    else:
        print('Precisa ler mais, reposta errada!')

    print('\n')
    
print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')
