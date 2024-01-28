#HERANCA
print("\n Exemplo herança")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")

    def emitir_som(self):
        pass

#Criando classe com heranca
class Cachorro(Animal):
    def emitir_som(self): #isso e polimorfismo pois usa o metodo da calsse mae porem implementado de outra forma
        return "au au"

#Criando classe com heranca
class Gato(Animal):
    def emitir_som(self): #isso e polimorfismo pois usa o metodo da calsse mae porem implementado de outra forma
        return "Miau"
    
print("\n Exemplo de poliformismo")
dog = Cachorro(nome="xurras")
cat = Gato(nome="felix")

animais = [dog, cat]
for animal in animais:
    print(f"animal {animal.nome} faz {animal.emitir_som()}") 

#ENCAPSULAMENTO
print("EXEMPLO DE ENCAPSULAMENTO")

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado __ so a classe pode mexer - so os metodos tem acesso
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000.00)
print(f"Saldo da conta: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta: {conta.consultar_saldo()}")
conta.sacar(valor=500)
print(f"Saldo da conta: {conta.consultar_saldo()}")

#ABSTRACAO - n permite criar objeto direto dela - e molde para outras classes
print("EXEMPLO DE ABSTRACAO")

from abc import ABC, abstractmethod
class Veiculo(ABC): #Define como abstrata

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

#cria classe carro derivando do abstrato 
class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"
    
carro_amarelo = Carro()
print(f"Carro amarelo: {carro_amarelo.ligar()}")
print(f"Carro amarelo: {carro_amarelo.desligar()}")