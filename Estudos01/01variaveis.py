brigadeiro = int(input('digite a quantia de brigadeiro ')) 
beijinho = int(input('digite o número de beijinho '))
coxinha = int(input('digite o número de coxinha '))
convidados = int(input('digite o número de convidados '))
soma = brigadeiro + beijinho 
#caso não tivéssemos especificado 'int' os números seriam reconhecidos como string e o resultado seria junção visual deles e não a soma

if coxinha < convidados or soma < convidados:
    print('certeza que vai dar quebra pau')
elif coxinha == convidados and soma == convidados:
    print('dá na estica')
else:
   print('me chama que eu vou')

print('Pense bem se vai chamar {} convidados!'.format(convidados))
print('terá {} docinhos.'.format(soma))

#no VS Code se tentar só 'run code' o input não vai funcionar, é necessário selecionar o 'Run Python File in Terminal' 