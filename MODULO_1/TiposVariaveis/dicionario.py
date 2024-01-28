#DICIONARIO - Colecao NAO ORDENADA DE PARES CHAVE VALORES
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("MEU DICIONARIO DE EXEMPLO:", pessoa)

#Acessando valores por chave
print("pessoa['nome']", pessoa["nome"])
print("pessoa['idade']", pessoa["idade"])
print("pessoa['cidade']", pessoa["cidade"])

pessoa["sobrenome"] = "Silva" #Atribui uma nova chave
print("pessoa['sobrenome']", pessoa["sobrenome"])

pessoa["idade"] = 31 #atualiza atributo
print("pessoa['idade']", pessoa["idade"])

#removendo um par chave valor
del pessoa["sobrenome"]
print("pessoa apos remocao", pessoa)


#METODOS #keys(), values(), items()

#keys() - retorna as chaves
chaves = list( pessoa.keys() ) #faz o parser para lista
print("chaves", chaves)
print("chaves[0]", chaves[0])

#values()
valores = list(pessoa.values()) #parse
print("valores", valores)
print("valores[0]", valores[0])

#Metodo items - tupla de chave valores
itens = list(pessoa.items())
print("itens", itens)
print("itens[0]", itens[0])
print("itens[0][1]", itens[0][1])


