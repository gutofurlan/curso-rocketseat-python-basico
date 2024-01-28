# TUPLAS - COLECAO ORDENADA E IMUTAVEIS - ELA é ESTATICA
minha_tupla = (1, 2, 2, 3, 4)
print("minha_tupla", minha_tupla)

# acessar
print("minha_tupla[0]", minha_tupla[0])
print("minha_tupla[1:4]", minha_tupla[1:4])
print("minha_tupla[-1]", minha_tupla[-1])  # ultimo elemento

# METODOS
# count() - retona a qnt de vezes que o elemento aparece
contagem = minha_tupla.count(2)
print("minha_tupla.count(2)", contagem)  # qnnt de vezes q o 2 aparece

# index - retorna posicao do elemnto
indice = minha_tupla.index(3)
print("minha_tupla.index(3)", minha_tupla.index(3))
