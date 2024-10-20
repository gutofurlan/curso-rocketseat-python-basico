class MyClass:
    #Metodo publico
    def method_1(self) -> None :
        print("method 1")

    #Metodo privado - so pode acessar de dentro da classe
    def __method_2(self) -> None :
        print("method 2")

    def registry(self) -> None :
        print("registry")
        self.__verify()
        self.__insert_data()

    def __verify(self) -> None:
        print("Verificando se existe no banco")

    def __insert_data(self) -> None:
        print("Insert DATA")

obj = MyClass()
obj.method_1()