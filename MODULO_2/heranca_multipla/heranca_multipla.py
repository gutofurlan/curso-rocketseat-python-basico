class Animal():
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando"
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} esta voando"
    
#O morcego ele é mamifero e é uma ave
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem som ultrassonicos"
        #return super().emitir_som() ##Esse super chama a implementacao da classe mae
    
morcego = Morcego(nome="Batman")
#Acessando metodos da classe animal  depos da classe mamifero e ave
print(f"Morcego com o nome {morcego.nome} esta amamantando: {morcego.amamentar()}")
print(f"Morcego com o nome {morcego.nome} esta voando: {morcego.voar()}")
print(f"Morcego com o nome {morcego.nome} esta emitindo som: {morcego.emitir_som()}")