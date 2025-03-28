#USANDO O NETMIKO

from netmiko import ConnectHandler

HOST = "R1" 
USER = "cisco" 
PASS = "cisco" 
TYPE = "cisco_xe"

#ConnectHandler serve para iniciar uma sessão SSH
r1 = ConnectHandler(host=HOST, username=USER, password=PASS, device_type=TYPE)

#Ao rodarmos esse script usando 'python -i nome_do arquivo.py' num terminal linux, será feita a conexão SSH com o host, o argumento -i deixa o programa python aberto no terminal
#Podemos dar comandos em python para gerenciar a sessão, (fecha a conexão com exit()).Por exemplo:
r1.is_alive() #verifica se a conexão está ativa, retorna True ou False
r1.disconnect() #desconecta a sessão
r1.establish_connection() #reconecta a sessão
r1.send_command('comandovalido') #envia o comando ao dispositivo, use antes de outros comandos o comando "terminal length 0" para evitar que a saída do terminal seja paginada e a automação 'presa' esperando interação humana.
r1.r1.send_config_set('comando1', 'comando2') #o argumento pode ser uma lista de comandos também
