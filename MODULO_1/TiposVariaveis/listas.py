# LISTAS - COLECAO DE LEMENTOS ORDENADOS E MUTAVEIS

minha_lista = [1, 2, 3, 4, 5, "augusto", True, False]
print("MINHA LISTA EXEMPLO: ",minha_lista)

#Exibir os elemntos
print("MINHA LISTA EXEMPLO INDICE 0:", minha_lista[0])
print("MINHA LISTA EXEMPLO INDICE 5:", minha_lista[5])
print("MINHA LISTA FATIADA DO 1 AO 7:", minha_lista[1:7])
print("minha_lista[:6]", minha_lista[:6]) #fatia do começo ate o indice 5
print("minha_lista[1:]", minha_lista[1:]) #fatia do elemento 1 ate o final

minha_lista[0] = "python" # altera o valor
print("MINHA LISTA EXEMPLO:", minha_lista)



##PRINCIPAIS METODOS

#append(): adiciona um elemento no final da lista
minha_lista.append(6)
print("MINHA LISTA APOS O APPEND", minha_lista)

#metodo index - retorna o indice do primeiro mais o valor especificado
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

#Método insert - insere um elemento em um indice especifico
minha_lista.insert(2, 10) #adicona no indice 3 o 10
print("minha_lista.insert(2, 10)", minha_lista)

#Metodo pop - Remove e retorna elemento de indice especifico
elemento_removido = minha_lista.pop(3)
print("elemento_removido", elemento_removido)
print("minha_lista.pop(3)", minha_lista)

#Metodo remove - removr elemento especifico
minha_lista.remove(True)
print("minha_lista.remove(True)", minha_lista)

#metodo sort
minha_lista_para_sort = [3,6,9,1,4]
minha_lista_para_sort.sort() #so funciona se os elementos forem do mesmo tipo
print("minha_lista_para_sort",minha_lista_para_sort)