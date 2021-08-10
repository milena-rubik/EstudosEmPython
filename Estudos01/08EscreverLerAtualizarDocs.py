#Metodo 1 sem oferecer diretório
def escrever_arquivo(texto): 
    arquivo = open ('teste.txt', 'w') #Cria arquivo ou abre e sobrescreve caso exista com esse nome e extensão
    arquivo.write(texto) #Comando permite escrever o texto no arquivo
    arquivo.close()
    
def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a') #O 'a' ao invés do 'w' faz com que o arquivo seja atualizado ou criado, mas não sobrescrito por inteiro
    arquivo.write(texto)
    arquivo.close()


#Metodo 2 especificando o diretório
def escrever_aquivo_no_diretorio(texto):
    diretorio = diretorio = 'C:/Users/Milenuxa/Documents/Python estudos/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') #'r' diz que é para leitura
    texto = arquivo.read() #abre para leitura
    print(texto)


if __name__ == '__main__':
    escrever_arquivo('Testando escrita. \n')
    atualizar_arquivo('Testando atualizar. \n')
    incluir = 'Aleatório Aleatório\n\n'
    atualizar_arquivo(incluir)
