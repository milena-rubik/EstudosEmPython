
# Conversão Json e dicionário python. Ainda que a aparência seja semelhante, o tipo json é string, não conseguimos acessar os índices, é muito usado para armazenar / transferir dados em API. 

facts = {
    "hostname": "r1",
    "os_version": "16.09",
    "snmp_config": {
        "location": "California",
        "contact": "admin@cisco.com",
        "ro": "public",
        "rw": "private",
    },
    "interfaces": [
        {
            "name": "Gig05",
            "description": "Management",
            "ip_addr": "10.253.0.1",
        }
    ]
}
    
print(type(facts)) #o tipo será dicionário

import json #para podermos trabalhar com json é preciso importar esse módulo

#A função 'dump()' transforma py dict em json 
facts_str = json.dumps(facts, indent=4) 
print(facts_str)
print(type(facts_str)) #a saida será o tipo string

#A função 'loads()' transforma json em py dict
dado_json = '{"hostname": "r1", "uptime": "3 days"}' #entrada em json
print(dado_json)
print(type(dado_json)) #resultado string
dado_dict = json.loads(dado_json) 
print(dado_dict)
print(type(dado_dict)) #resultado dicionário
print(dado_dict["uptime"])
