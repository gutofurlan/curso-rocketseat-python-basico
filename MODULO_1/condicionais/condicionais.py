#CONDICIONAIS if, elif, else

idade = int( input("Quantos anos vc tem ?") )
if idade >= 18:
    print("MAIOR DE IDADE")
else:
    print("menor de idade")

if idade == 19:
    print("Voce tem 19 anos")

if idade != 10:
    print("Vc nao tem 10 anos")

if idade < 18:
    print("Voce é menor de idade")
elif idade == 27:
    print("Vc tem 27 anos")
else:
    print("ELSE")

mensagem = "Pode tirar a carteira" if idade >= 18 else "vc n pode"
print(mensagem)

