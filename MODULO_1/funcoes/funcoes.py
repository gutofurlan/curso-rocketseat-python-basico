#FUNCAO - Boloco de codigo reutilizado
def saudacao(nome):
    print(f"OLA {nome}")

print("\n chamaando funcao")
saudacao("Alice")
saudacao("Bob")

#Funcao de quarado de numero - funcao com retorno
def quadrado(numero):
    return numero ** 2

print("\n chamaando funcao quadrado de 2", quadrado(2))


#FUNCAO COM MULTIPLOS PARAMETROS
def soma(numero1, numero2):
    return numero1 + numero2

print("SOMA: ", soma(1,2))
