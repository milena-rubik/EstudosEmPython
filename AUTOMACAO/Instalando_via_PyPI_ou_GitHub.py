#Para instalar pacotes usando PyPI ou GitHub:

# Quando disponível no PyPI podemos usar o pip:

"""pip search <PACKAGE_NAME>: procura o pacote pelo nome em PyPI.

pip install <PACKAGE_NAME>: instala a última versão e dependências na máquina.

pip install <PACKAGE_NAME>==1.0.0: a mesma coisa que o de cima só que especificando a versão.

pip install ––upgrade <PACKAGE_NAME>: upgrade para última versão.

pip install –r <REQUIREMENTS_FILE>: instala todos os pacotes especificados em <REQUIREMENTS_FILE>.

pip uninstall <PACKAGE_NAME>: desinstala.

pip freeze: mostra e preserva as versões de pacotes atualmente instalados.

pip freeze –r <REQUIREMENTS_FILE>: mostra e preserva as versões de pacotes atualmente instalado usa a ordem dada no requirements file.

pip list: mostra pacotes instalados e suas versões.

pip list -o: lista pacotes com outdate."""


#Quando não disponíveis no PyPI:

"""Pode clonar código do GitHub usando o comando git
Exemplo:
    student@vm:~$ git clone https://github.com/ktbyers/netmiko.git netmiko
o argumento clone copia o repositório para um novo diretório criado, a palavra/argumento 'netmiko' após o path nomeia esta pasta diretório.

Instalando:
    student@student-vm:~/netmiko$ python setup.py install

Após isso deve ser possível usar o pacote no python com o 'import'"""
    
