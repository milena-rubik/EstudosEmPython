Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #! /usr/bin/env python
... # Essa linha (shebang) indica que o script deve ser executado usando o interpretador Python disponível no ambiente do usuário.
... 
... import requests
... import json
... # Importa os módulos `requests` (para fazer requisições HTTP) e `json` (para manipulação de dados em formato JSON).
... 
... # Check for module dependencies:
... # Verifica se todos os módulos necessários estão instalados.
... not_installed_modules = []
... # Cria uma lista para armazenar os módulos que não estão instalados.
... 
... try:
...     from requests.auth import HTTPBasicAuth
...     # Tenta importar HTTPBasicAuth do módulo requests (para autenticação HTTP básica).
... except ImportError:
...     not_installed_modules.append("requests")
...     # Se falhar, adiciona "requests" à lista de módulos ausentes.
... 
... try:
...     import yaml
...     # Tenta importar o módulo yaml (usado para lidar com arquivos YAML).
... except ImportError:
...     not_installed_modules.append("PyYAML")
...     # Se falhar, adiciona "PyYAML" à lista de módulos ausentes.
... 
... if not_installed_modules:
...     # Se houver algum módulo faltando...
...     print("Please install following Python modules:")
...     # Informa ao usuário que deve instalar os módulos abaixo.
... 
...     for module in not_installed_modules:
...         print("  - {module}".format(module=module))
...         # Exibe o nome de cada módulo ausente.
... 
...     sys.exit(1)
...     # Encerra o programa com código de erro 1, indicando que algo deu errado (módulos ausentes).
... 
... 
