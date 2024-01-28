#decorador - adicionar funcionalidade em uma funcao (tipo middleware)
from typing import Any


def meu_decorador(func): #passa a funcao que vai receber
    def wrapper(): #serve para definir oque ira acontecer antes ou depois da funcao - ele embrula a funcao
        print("Antes da funcao ser chamada")
        func()
        print("Depois da funcao ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha funcao foi chamada")

minha_funcao()


#DECORADOR DE CLASS
class MeuDecoradorDeClasse():
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Antes da funcao ser chamada - decorador de calsse")
        self.func()
        print("Depois da funcao ser chamada - decorador de calsse")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao")

segunda_funcao()