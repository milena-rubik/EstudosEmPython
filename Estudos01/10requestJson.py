import requests

cepbuscado = input('Informe o CEP (apenas números): ')
site = 'https://viacep.com.br/ws/'+ cepbuscado + '/json/' 
cepinfo = requests.get(site) #requisita as informações daquele link e atribui a cepinfo
print(cepinfo.json()) #imprime as informações gerais relacionadas ao cep buscado
cepdicionario = cepinfo.json() #procedimento necessário para poder manipular ocnforme abaixo, chamar as informações separadas...
print(type(cepdicionario)) #mostra que a variável é tipo dicionário
print(cepdicionario['logradouro']) #imprime a informação requisitada
print(cepdicionario['bairro'])