#modulos- arquivos q tem funcoes e instrucao que podemos impoerar e usar
print("Exemplo de importacao de modulo padrao")

# import math # importou o modulo inteiro
# raiz_quadrada = math.sqrt(25)

from math import sqrt # importou so o srt do math
raiz_quadrada = sqrt(25)
print(raiz_quadrada)

print("\n Exemplo de criacao e utilizacao de um modulo personalizado")

# import meu_modulo
# meu_modulo.saudacao("Augusto")
# print("DOBRO DE 2:", meu_modulo.dobro(2))

from meu_modulo import saudacao, dobro
saudacao("Augusto")
print("DOBRO DE 2:", dobro(2))