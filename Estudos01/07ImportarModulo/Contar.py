def ContarCaracter(lista): #declara método
    contador = []
    for x in lista: #percorre os itens da lista
        numerocaracter = len(x) #conta as letras do item de índice x
        contador.append(numerocaracter) #adiciona na lista contador o número de letras do item de índice x na posição x
    return contador #retorna a lista com a quantia de caracter de cada item da lista

if __name__ == '__main__': #ideal para uso em testes dentro do módulo, pois faz com que trecho de código não seja exportado quando módulo chamado em outros arquivos
    listaflor = ['azaleia', 'rosa', 'margarida']
    print(ContarCaracter(listaflor))