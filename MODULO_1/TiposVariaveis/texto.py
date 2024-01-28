#Declaracao
nome_completo = "Augusto Furlan" # pode ser aspas simples ''
nome_completo_aspas = """
Augusto 
Furlan
"""
nome_completo_quebra = "Augusto " \
                       "Furlan"

nome = "Augusto"
sobrenome = "Furlan"
print("STRING: ", nome_completo)
print("TYPE STRING: ", type(nome_completo))

#FORMATACAO
print("Nome completo (1a forma) ", nome_completo) #concatena com a var
print("Nome completo (2a forma) " + nome_completo) #concatena com +
print("Nome completo (3a forma) " + "Augusto " + "Furlan") #concatena com + multiplas strings
print("Nome completo (4a forma) " + "Augusto", "Furlan") #concatena com + multiplas strings
print("Nome completo (5a forma) ", nome_completo_aspas)
print("Nome completo (6a forma) ", nome_completo_quebra)
print("Nome completo (7a forma) %s " % nome) # Faz troca pelo %s
print("Nome completo (8a forma) %s %s " % (nome, sobrenome) ) # MAIS SEGURA POIS JA É DEFINIDO O TIPO -  Faz troca pelo %s qnd tem mais q uma tem q ter o ()
print(f"Nome completo (9a forma) : {nome} {sobrenome} ") # Faz troca pelo da string pelo {} porem precisa do f no comço
print("Nome completo (10a forma) : {} {} ".format(nome, sobrenome)) # Faz troca pelo da string pelo {} porem n precisa passar o f no começo

#METODOS

#upper tudo em maiusculo e lower tudo minisculo
print( nome.upper() ) # ele nao trocou o conteudo ele so exibe desse modo
print( nome.lower() ) # ele nao trocou o conteudo ele so exibe desse modo

#ACESSAR CARACTER ESPECIFICO
print(nome[0]) #igual array

#count e find
print( nome_completo.count("u") ) # conta quantas vezes a string do count aparece
print( nome_completo.find("u") ) # retorna a primeira posicao que aparece

#CODIFICACAO
#encode
print(nome.encode()) #string porem em formato de byte
print(nome.encode().decode()) #string porem em formato de string ele decodifica

#replace - substituir valores da string
print(nome_completo.replace("u", "x")) # troca tudo que é u para x
telefone = "(19)97325-0502"
print( telefone.replace("(", "").replace(")", "").replace("-", "") )

#FUNCAO JOIN e SPLIT

#join separa cada caracter
print( "-".join(nome_completo) )

#split - divide, transforma string em lista
print( nome_completo.split(" ") )

#strip - REMOVER TUDO QUE ESTA NO COMECO E TUDO QUE ESTA NO FINAL REFERENTEAO ALVO
teste_strip = "xAugusto Furlanx"
print( teste_strip.strip("x") ) #So remove do inicio e fim
print( teste_strip.rstrip("x") ) #So remove do inicio e fim - do da direita
print( teste_strip.lstrip("x") ) #So remove do inicio e fim - do da esquerda

#COMPARADORES

#startswith - sabe se comeca com um eterminado texto
print(nome_completo.startswith("Au")) # se for au ele n pegap ois o a é minusculo
print(nome_completo.startswith("Be")) # se for au ele n pegap ois o a é minusculo

#in e notin - saber we existe um termo no meio
print( "gus" in nome_completo ) # se existe
print( "gus" not in nome_completo ) # se nao existe
