conjunto1 = {1994, 1995, 1996, 1997} #declara conjunto
print('Conjunto 1 {}'.format(conjunto1))
conjunto2 = {1997, 1998, 1999, 2000}
print('Conjunto 2 {}'.format(conjunto2))
conjunto3 =  {1994, 1995, 1996, 1997, 1998}
print('Conjunto 3 {}\n\n'.format(conjunto3))
conjuntounido = conjunto1.union(conjunto2) #une os conjuntos 1 e 2 no conjuntouniao
print('União dos conjuntos 1 e 2 {}'.format(conjuntounido))
conjuntointerseccao = conjunto1.intersection(conjunto2) #faz a intersecção entre conjunto 1 e 2
print('Intersecção dos conjuntos 1 e 2 {}'.format(conjuntointerseccao))
conjuntodiferenca = conjunto1.difference(conjunto2) #inclui o que há apenas no conjunto1 ao conjuntodiferenca
print('Diferença do conjunto 1 em relação ao 2 {}'.format(conjuntodiferenca))
conjuntodifdosdois = conjunto1.symmetric_difference(conjunto2) #inclui em conjuntodifdosdois o que 1 e 2 não tem em comum
print('Diferenças entre o conjunto 1 e 2 {}\n'.format(conjuntodifdosdois))

conjuntosub = conjunto1.issubset(conjunto3) #testa a condição se 1 é subconjunto de 3
print('O conjunto 1 é um subconjunto de 3? {}'.format(conjuntosub))
conjuntosuper = conjunto3.issuperset(conjunto1)  #testa a condição se 3 é superconjunto de 1
print('Então o conjunto 3 é um superconjunto de 1? {}\n\n'.format(conjuntosuper))

listamercado = ['sabão', 'leite', 'ovo', 'leite']
print(listamercado)
conjuntomercado = set(listamercado) #transforma lista em conjunto e remove duplicidades
print(conjuntomercado)
listamercado = list(conjuntomercado) #converte conjunto em lista
print(listamercado)