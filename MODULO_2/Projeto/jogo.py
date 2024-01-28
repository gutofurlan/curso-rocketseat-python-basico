import random

#Personagem (classe mae)
#heroi herda do personagem
#inimigo - Classe do adversario

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"NOME: {self.get_nome()}\nVIDA: {self.get_vida()}\nNIVEL: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano

        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) #Valor do atawue atraves de random
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")




#Classe de Heroi
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self): #Exibe detalhes do heroi
        return f"{super().exibir_detalhes()} \nHABILIDADE: {self.get_habilidade()} \n"

    def ataque_especial(self, alvo): #O Ataque especial é referente apenas ao heroi
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8) #Dano atraves do random int
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade {self.get_habilidade()} no {alvo.get_nome()} e causou {dano} de dano!")

#Classe de Inimigo
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nTIPO: {self.get_tipo()} \n"


class Jogo: #Oquestra o jogo dos turnos

    def __init__(self):
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")

    def iniciar_batalha(self): #Faz gestao de batalha em turno
        print("*** INICIANDO BATALHA ***")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagem:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar")
            escolha = input("Escolha (1- Ataque Normal, 2- Ataque Especial)")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("ESCOLHA INVALIDA, escolha novamente")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi) # INIMIGO ATAA HEROI


        if self.heroi.get_vida() > 0:
            print("\nPARABENS, VOCE VENCEU A BATALHA!")
        else:
            print("\nVOCE FOI DERROTADO!")



#Ceiar instwncia do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()

# heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
# print(heroi.exibir_detalhes())
#
# inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")
# print(inimigo.exibir_detalhes())