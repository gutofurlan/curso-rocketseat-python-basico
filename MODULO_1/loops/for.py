##Intera sobre sequencia de elemento
lista = [1,2,3,4,5]
for elemento in lista:
    print("ELEMENTO", elemento)

#for de tupla
tupla = (1,2,3,4,5,6)
for elemento in tupla:
    print(elemento)

#for no dicionario
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

#chaves
for chave in pessoa.keys():
    print("chave", chave)

#valores
for value in pessoa.values():
    print("value", value)

#chave valor
for chave, valor in pessoa.items():
    print(f"CHAVE: {chave} VALOR: {valor}")

#range() - intervalo numero atraves de lista
print("range(0,10)", list(range(0,10)))

for enumero in range(5):
    print("NUMERO", enumero)

#UTILIZANDO RANGE COM LEN
lista = [1,2,3,4,5]
for indice in range(0, len(lista)):
    print("INDICE:", indice)
    print("ELEMENTO:", lista[indice])

#enumerate() - permite usar a lista extraindo o indice e valor
lista_enumerate = ["a","b","c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"INDICE {indice} VALOR: {valor}")