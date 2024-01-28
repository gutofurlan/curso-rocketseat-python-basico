#Classe é algo do mundo real

#Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None: # o none é q n retorna nada
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Ola sou {self.nome} e tenho {self.idade} anos"

#objetos 
pessoa1 = Pessoa("Alice", 30)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.saudacao())