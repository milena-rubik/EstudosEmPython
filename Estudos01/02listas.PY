#LISTAS

numeros = [33,1,55,67]
animais = ['cachorro', 'gato', 'vaca']

print(min(numeros)) #imprime o menor número da lista
print(max(numeros)) #imprime o maior número da lista
numeros.sort() #ordena a lista
print(numeros)
numeros.reverse() #inverte a ordem da lista
print(numeros)
numeros.pop() #retira ultimo item da lista, mas posso inserir o indice do item, com '.remove' posso colocar o conteudo
print(numeros)


for x in animais: #percorre a lista
    print(x)  
    
if 'porco' in animais:
    print('tem um porco na lista!')
else:
    print('será que o porco virou bacon?')
    animais.append('porco') #inclui o item na lista
    print(animais)

animais = tuple(animais) #converte lista em tupla
print(type(animais))
animais = list(animais) #converte tupla em lista
print(type(animais))