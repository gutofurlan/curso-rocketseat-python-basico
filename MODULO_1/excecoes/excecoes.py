print("Exemplo de captura de excecoes")

try:
    numero = int(input("DIGITE UM NUMERO INTEIRO: "))
    resultado = 10 / numero
except ValueError as e:
    print("ERRO VALUE ERRO", e)
except Exception as e:
    print("ERRO:", e)
else: #so executa se deu certo
    print("Executa se deu certo")
finally: #Ocorre independente de sucesso ou n
    print("Operação finalizada")

print("RESULTADO:", resultado)