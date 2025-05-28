#Comentários do LAB 'Consume HTTP-Based APIs with Python Requests' do curso

#! /usr/bin/env python # Indica que o script deve ser executado usando o interpretador Python disponível no ambiente do sistema.

import requests  # Importa o módulo requests, utilizado para fazer requisições HTTP.
import json      # Importa o módulo json, utilizado para manipular dados no formato JSON.

not_installed_modules = [] # Lista que armazenará os módulos que não estão instalados

# Tenta importar a função HTTPBasicAuth do módulo requests.auth
try:
    from requests.auth import HTTPBasicAuth
except ImportError:
    # Se não conseguir importar, adiciona 'requests' à lista de módulos não instalados
    not_installed_modules.append("requests")

# Tenta importar o módulo PyYAML (como 'yaml')
try:
    import yaml
except ImportError:
    # Se não conseguir importar, adiciona 'PyYAML' à lista
    not_installed_modules.append("PyYAML")

# Se houver módulos não instalados, avisa o usuário e encerra o programa
if not_installed_modules:
    print("Please install following Python modules:")
    for module in not_installed_modules:
        print("  - {module}".format(module=module))
    sys.exit(1)  # Encerra o script com código de erro 1 (indicando falha)

# Cabeçalhos HTTP padrão utilizados nas requisições RESTCONF
HTTP_HEADERS = {
    "Content-Type": "application/yang-data+json",  # Tipo do conteúdo enviado
    "Accept": "application/yang-data+json",        # Tipo de resposta esperada
}

# Autenticação HTTP básica com usuário e senha padrão (cisco/cisco)
HTTP_AUTH = HTTPBasicAuth("cisco", "cisco")

# Função que retorna um inventário de dispositivos e credenciais
def get_inventory():
    inventory = {
        "r1": {"username": "cisco", "password": "cisco"},
        "r2": {"username": "cisco", "password": "cisco"},
    }
    return inventory

# Função para obter o número de série de um dispositivo
def get_serial_data(host):
    url = "https://{host}/restconf/data/Cisco-IOS-XE-native:native/license/udi/sn".format(host=host)
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = json.loads(response.text)  # Converte a resposta JSON em dicionário Python
    serial_data = result["Cisco-IOS-XE-native:sn"]  # Extrai o número de série
    return serial_data

# Função para obter a versão do sistema operacional de um dispositivo
def get_version_data(host):
    url = "https://{host}/restconf/data/Cisco-IOS-XE-native:native/version".format(host=host)
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = response.json()  # Converte a resposta JSON diretamente
    version_data = result["Cisco-IOS-XE-native:version"]  # Extrai a versão
    return version_data

# Função para obter o nome (hostname) de um dispositivo
def get_hostname(host):
    url = "https://{host}/restconf/data/Cisco-IOS-XE-native:native/hostname".format(host=host)
    response = requests.get(url, headers=HTTP_HEADERS, auth=HTTP_AUTH, verify=False)
    result = json.loads(response.text)  # Converte JSON em dicionário Python
    hostname = result.get("Cisco-IOS-XE-native:hostname")  # Obtém o hostname (se existir)
    return hostname

# Função que organiza os dados coletados dos dispositivos
def structure_data():
    devices = {}  # Dicionário para armazenar dados de cada dispositivo
    net_inventory = get_inventory()  # Obtém a lista de dispositivos
    for host in net_inventory:
        devices[host] = {}  # Cria uma entrada para cada host
        devices[host]["serial_number"] = get_serial_data(host)  # Adiciona número de série
        devices[host]["os_version"] = get_version_data(host)    # Adiciona versão do sistema
        devices[host]["hostname"] = get_hostname(host)          # Adiciona hostname
    return devices  # Retorna o dicionário completo com os dados

# Função principal do programa
def main():
    structured_data = structure_data()  # Coleta e estrutura os dados dos dispositivos

    # Cria um cabeçalho formatado para a tabela
    heading = "| {:^10} | {:^10} | {:^15} | {:^12} |".format(
        "Device", "Hostname", "Serial Number", "OS Version"
    )
    print(len(heading) * "-")  # Linha horizontal
    print(heading)             # Cabeçalho da tabela
    print(len(heading) * "-")  # Linha horizontal
    for hostname, details in structured_data.items():  # Itera sobre os dispositivos
        print(
            "| {:^10} | {:^10} | {:^15} | {:^12} |".format(
                hostname,
                details["hostname"],
                details["serial_number"],
                details["os_version"],
            )
        )
        print(len(heading) * "-")  # Linha separadora após cada linha da tabela

# Executa a função principal se o script for rodado diretamente
if __name__ == "__main__":
    main()
