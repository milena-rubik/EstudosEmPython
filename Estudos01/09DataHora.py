from datetime import date, time, datetime, timedelta
from typing import Tuple


#referente a importação date:
datahoje = date.today()
print(datahoje) #no formato padrão ano-mes-dia
#podemos formatar como queremos através das diretivas de datetime tem na documentacao https://docs.python.org/pt-br/3/library/datetime.html exemplos:
print(datahoje.strftime('%d/%m/%Y')) 
print(datahoje.strftime('%A'))


#referente a importação time
horarioteste = time(hour=12, minute=30, second=15)
print(horarioteste) #imprime no formato hora:minuto:segundo


#referente a importação datetime
agora = datetime.now() #captura o dia e a hora atual
print(agora)
print(agora.strftime('%d/%m/%y - %H:%M'))
tuplasemana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
print(tuplasemana[agora.weekday()]) #weekday retorna o dia da semana em número de 0 a 6

dataemstring = '10/12/2020'
dataconvertida = datetime.strptime(dataemstring, '%d/%m/%Y') #faz a conversão de string para datetime, informar o formato que está a string nesse caso '%d/%m/%Y'
novadata = dataconvertida - timedelta(days=365) #subtrai x dias em uma data, possivel inserir inforações também de minutos, horas...
print(novadata)