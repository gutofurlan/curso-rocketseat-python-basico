# valida se escolha do menu é permitida
def capturar_e_validar_escolha_do_menu() -> int:
    while True:
        try:
            opcao = int(input("Escolha a opção desejada: "))

            if opcao not in list(range(1, 8)):
                print("OPCAO INVALIDA, ESCOLHA UMA OPCAO VALIDA")
            else:
                break
        except Exception as e:
            print("OPCAO INVALIDA, ESCOLHA UMA OPCAO VALIDA")

    return opcao

#Recupera o indice da lista onde esta o contato
def capturar_e_validar_id_do_contato(agenda) -> int:

    while True:
        try:
            opcao = int(input("Escolha o contato: "))

            if opcao not in list(range(1, len(agenda)) ):
                print("CONTATO INVALIDO, ESCOLHA UM CONTATO VALIDO")
            else:
                break
        except Exception as e:
            print("CONTATO INVALIDO, ESCOLHA UM CONTATO VALIDO")
    opcao -= 1
    return opcao

# valida campo nome
def validar_e_capturar_campo_nome() -> str:
    while True:
        campo = input("Digite o nome: ")
        if (campo == ""):
            print("O nome é pbrigatório")
        else:
            return campo


# valida campo telefone
def validar_e_capturar_campo_telefone():
    while True:
        try:
            campo = input("Digite o telefone: ")
            campo = int(campo.replace("-", "").replace("(", "").replace(")", ""))
            if (campo == ""):
                print("O telefone é pbrigatório")
            else:
                return campo
        except Exception as e:
            print("TELEFONE INVALIDO, DIGITE UM TELEFONE VALIDO")


# valida campo email
def validar_e_capturar_campo_email():
    while True:
        campo = input("Digite o email: ")
        if campo == "":
            print("O email é pbrigatório")
        elif "@" not in campo or "." not in campo or "," in campo:
            print("DIGITE UM EMAIL VÁLIDO")
        else:
            return campo


# valida campo favorito
def validar_e_capturar_campo_favorito() -> bool:
    while True:
        campo = input("Esse contato é favorito (S/N): ")
        if campo.upper() not in ["S", "N"]:
            print("Formato inválido")
        else:
            if campo.upper() == "S":
                return True
            else:
                return False

#ordena lista pelo nome
def ordenar_lista_pelo_nome_do_contato(agenda) -> list:
    agenda = sorted(agenda, key=lambda x: x['nome'])
    return agenda
