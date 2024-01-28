import modulo_agenda

agenda = []#lista com todos os contatos
#contato {"nome", "telefone, "email", "favorito"} #dicionario para contato


#Ira fazer o cadastro de um novo contato na agenda
def adicionar_contato_na_agenda(agenda):
    nome = modulo_agenda.validar_e_capturar_campo_nome()
    telefone = modulo_agenda.validar_e_capturar_campo_telefone()
    email = modulo_agenda.validar_e_capturar_campo_email()
    favorito = modulo_agenda.validar_e_capturar_campo_favorito()
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}

    agenda.append(contato)
    modulo_agenda.ordenar_lista_pelo_nome_do_contato(agenda)

#Exibe os contatos
def exibir_lista_de_contatos(agenda : list, apenas_favorito : bool = False) -> None:

    indice_caso_for_apenas_favorito = 1
    for indice, contato in enumerate(agenda, start=1):

        mensagem = ( f"{indice_caso_for_apenas_favorito}" if apenas_favorito else f"{indice}" ) + f" - Nome: {contato['nome']} | Telefone: {contato['telefone']} | E-mail: {contato['email']} | Favorito: [" + ( "✔" if contato['favorito'] else "" ) + "]"

        if(apenas_favorito and contato['favorito']):
            print(mensagem)
            indice_caso_for_apenas_favorito +=1
        elif apenas_favorito == False:
            print(mensagem)

#Editar contato
def editar_contato(agenda) -> None :
    exibir_lista_de_contatos(agenda=agenda)
    id = modulo_agenda.capturar_e_validar_id_do_contato(agenda)
    nome = modulo_agenda.validar_e_capturar_campo_nome()
    telefone = modulo_agenda.validar_e_capturar_campo_telefone()
    email = modulo_agenda.validar_e_capturar_campo_email()
    favorito = modulo_agenda.validar_e_capturar_campo_favorito()
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}

    agenda[id] = contato
    modulo_agenda.ordenar_lista_pelo_nome_do_contato(agenda)

    print("\n CONTATO ATUALIZADO COM SUCESSO")

#Marcar/Desmarcar contato cmo favorito
def marcar_desmarcar_contato_como_favorito(agenda) -> None:
    exibir_lista_de_contatos(agenda=agenda)
    id = modulo_agenda.capturar_e_validar_id_do_contato(agenda)
    contato = agenda[id]
    contato["favorito"] = not contato["favorito"]
    agenda[id] = contato

#remove o contato da agenda
def remover_contato(agenda) -> None:
    exibir_lista_de_contatos(agenda=agenda)
    id = modulo_agenda.capturar_e_validar_id_do_contato(agenda)
    contato_para_remover = agenda[id]
    agenda.remove(contato_para_remover)
    print("CONTATO REMOVIDO COM SUCESSO")

while True:
    print("\n \n*** DESAFIO AGENDA ***")
    print("1 - Adicionar contato")
    print("2 - Visualizar agenda")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar contato como favorito")
    print("5 - Exibir lista de favoritos")
    print("6 - Apagar contato")
    print("7 - Sair")

    opcao = modulo_agenda.capturar_e_validar_escolha_do_menu()

    if opcao == 1:
        adicionar_contato_na_agenda(agenda)
    elif opcao == 2:
        exibir_lista_de_contatos(agenda=agenda, apenas_favorito=False)
    elif opcao == 3:
        editar_contato(agenda=agenda)
    elif opcao == 4:
        marcar_desmarcar_contato_como_favorito(agenda=agenda)
    elif opcao == 5:
        exibir_lista_de_contatos(agenda=agenda, apenas_favorito=True)
    elif opcao == 6:
        remover_contato(agenda=agenda)
    elif opcao == 7:
        print("*** OBRIGADO POR USAR O SISTEMA ***")
        break
