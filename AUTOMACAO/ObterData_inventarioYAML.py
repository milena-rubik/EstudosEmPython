#Comentário lab aula API Cisco

#!/usr/bin/env python
# Indica que o script deve ser executado com o interpretador Python do ambiente.

import requests       # Usado para enviar requisições HTTP (comunicação com RESTCONF).
import json           # Usado para manipular dados JSON (converter entre string e dicionário).
import sys            # Usado para encerrar o programa em caso de erro.

# Lista para armazenar os nomes dos módulos não instalados
not_installed_modules = []

# Verifica se o módulo requests (e sua subbiblioteca HTTPBasicAuth) está disponível
try:
    from requests.auth import HTTPBasicAuth
except ImportError:
    not_installed_modules.append("requests")

# Verifica se o módulo PyYAML está disponível
try:
    import yaml
except ImportError:
    not_installed_modules.append("PyYAML")

# Se algum módulo estiver faltando, avisa o usuário e encerra o script
if not_installed_modules:
    print("Please install the following Python modules:")
    for module in not_installed_modules:
        print("  - {}".format(module))
    sys.exit(1)

# Define os cabeçalhos HTTP para as requisições RESTCONF
HTTP_HEADERS = {
    "Content-Type": "application/yang-data+json",  # Tipo de dado enviado
    "Accept": "application/yang-data+json",        # Tipo de resposta esperada
}

# Define as credenciais de autenticação (usuário/senha)
HTTP_AUTH = HTTPBasicAuth("cisco", "cisco")

# Desativa os avisos de certificado SSL inválido (porque usamos verify=False)
requests.packages.urllib3.disable_warnings()

# Função que lê o arquivo de inventário YAML e retorna um dicionário com os dispositivos
def get_inventory():
    inventory_file = "inventory.yml"  # Nome do arquivo YAML
    with open(inventory_file) as fh:  # Abre o arquivo para leitura
        inventory = yaml.safe_load(fh)  # Converte o YAML em dicionário Python
    return inventory

# Função que consulta o número de série do dispositivo via RESTCONF
def get_serial_data(host):
    url = (
        "https://{host}/restconf/data/Cisco-IOS-XE-native:native"
        "/license/udi/sn".format(host=host)
    )
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = json.loads(response.text)
    serial_data = result["Cisco-IOS-XE-native:sn"]
    return serial_data

# Função que consulta a versão do sistema operacional via RESTCONF
def get_version_data(host):
    url = "https://{host}/restconf/data/Cisco-IOS-XE-native:native/version".format(host=host)
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = json.loads(response.text)
    version_data = result["Cisco-IOS-XE-native:version"]
    return version_data

# Função que consulta o hostname do dispositivo via RESTCONF
def get_hostname(host):
    url = "https://{host}/restconf/data/Cisco-IOS-XE-native:native/hostname".format(host=host)
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = json.loads(response.text)
    hostname = result.get("Cisco-IOS-XE-native:hostname")
    return hostname

# Função que estrutura os dados coletados de todos os dispositivos
def structure_data():
    devices = {}  # Dicionário onde os dados serão organizados
    net_inventory = get_inventory()  # Lê o inventário YAML

    for host in net_inventory:  # Itera sobre cada host
        devices[host] = {}  # Cria uma entrada para o host
        devices[host]["os_version"] = get_version_data(host)  # Coleta versão do SO
        devices[host]["serial_number"] = get_serial_data(host)  # Coleta número de série
        devices[host]["hostname"] = get_hostname(host)  # Coleta hostname

    return devices  # Retorna os dados organizados

# Função principal que exibe os dados em formato de tabela
def main():
    heading = "|{:^10} | {:^10} | {:^12} | {:^15}|".format(
        "Device", "Hostname", "OS Version", "Serial Number"
    )
    print(len(heading) * "-")  # Linha separadora
    print(heading
