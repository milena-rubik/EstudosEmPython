#Curso da DIO Python Básico.

import shutil #necessário para os metodos de copiar e mover arquivos

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
    diretorio = 'C:/Users/Milenuxa/Documents/Python estudos/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') #'r' diz que é para leitura
    texto = arquivo.read() #abre para leitura
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n') #cria uma lista, gera os itens tendo como corte o inserido, nesse caso quebra de linha, ou seja cada linha do arquivo será item da lista
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        print(aluno)
        lista_notas.pop(0) #retira o elemento de posição 0
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:\Users\Milenuxa\Documents\Python estudos\Estudos01\testes') #copia o arquivo para o diretório informado
 
def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:\Users\Milenuxa\Documents\Python estudos\Estudos01\testes')
 

 
if __name__ == '__main__': #ideal para uso em testes dentro do módulo, pois faz com que trecho de código não seja exportado quando módulo chamado em outros arquivos 
    escrever_arquivo('Testando escrita. \n')
    atualizar_arquivo('Testando atualizar. \n')
    incluir = '\n\nAleatório Aleatório\n\n'
    atualizar_arquivo(incluir)

    escrever_arquivo('Primeira linha. \n')
    aluno = 'Joao, 7, 8 , 9'
    lista_media = media_notas('notas.txt')
    print(lista_media)
