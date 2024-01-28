#@classmethod
#@staticmethod

class MinhaClasse():
    valor = 10 #Atributo Global da classe
    def __init__(self, nome) -> None:
        self.nome = nome
    
    #requer uma instancia
    def metodo_de_instancia(self):
        return f"Metodo de instancia chamado para {self.nome} - valor: {self.valor}"
    
    #metodo de classe - cls é a class - tem acesso aos atributos e metodos
    @classmethod
    def metodo_da_classe(cls):
        return f"Metodo da classe {cls.valor}"
    
    #Ele n tem acesso a class nem a propriedades
    @staticmethod
    def metodo_estatico():
        return f"Metodo estico"


obj = MinhaClasse("Augusto")
print(obj.metodo_de_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_da_classe())
print(MinhaClasse.metodo_estatico())


class Carro():
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

carro1 = Carro.criar_carro("Toyota,Corolla,2022")
print(f"CARRO CRIADO ATRAVES DA INSTNACIA - {carro1.marca} - {carro1.modelo}, {carro1.ano}")