brigadeiro = input('digite a quantia de brigadeiro ') 
beijinho = input('digite o número de beijinho ')
coxinha = input('digite o número de coxinha ')
convidados = input('digite o número de convidados ')
soma = brigadeiro + beijinho

if coxinha < convidados or soma < convidados:
    print('certeza que vai dar quebra pau')
elif coxinha == convidados and soma == convidados:
    print('dá na estica')
else:
   print('me chama que eu vou')

print('Pense bem se vai chamar {} convidados!'.format(convidados))

#no VS Code se tentar só 'run code' o input não vai funcionar, é necessário selecionar o 'Run Python File in Terminal' 