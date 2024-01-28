def adicionar_tarefa(tarefas, nome_tarefa="tarefa padrão"):
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"TAREFA {nome_tarefa} adiconada com sucesso")
    return

def ver_tarefas(tarefas):
    print("\n Lista de tarefas:")

    for indice, tarefa in enumerate(tarefas, start=1): #esse start ele inicia no 1
        status = "Completada" if tarefa["completada"] else ""
        print(f"{indice} - {tarefa['nome']} - [{status}]")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa="tarefa padrão"):
    indice_tarefa = indice_tarefa - 1 # diminui 1 poiso indice comeca no 0 e n no 1 como exibimos

    #valida se existe o indice da tarefa
    if indice_tarefa >= 0 and indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["nome"] = novo_nome_tarefa
        print(f"TAREFA {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("INDICE DE TAREFA INVALIDO")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa = indice_tarefa - 1 # diminui 1 poiso indice comeca no 0 e n no 1 como exibimos

    #valida se existe o indice da tarefa
    if indice_tarefa >= 0 and indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["completada"] = True
        print(f"TAREFA {indice_tarefa} - {tarefas[indice_tarefa]['nome']} marcada como completo")
    else:
        print("INDICE DE TAREFA INVALIDO")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)

        print("Tarefas removidas com sucesso")
    return


tarefas = [] # onde armazena as tarefas
#menu
while True:
    print("*** MENU GERENCIADOR DE TAREFAS ***")
    print("1 - ADICIONAR TAREFA")
    print("2 - VER TAREFAS")
    print("3 - ATUALIZAR TAREFA")
    print("4 - COMPLETAR TAREFA")
    print("5 - DELETAR TAREFAS COMPLETADAS")
    print("6 - SAIR")
    escolha = input("Escolha sua opçao: ")

    if int(escolha) == 1:
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa=nome_tarefa)
    elif int(escolha) == 2:
        ver_tarefas(tarefas)
    elif int(escolha) == 3:
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa que deseja atualizar: ")
        nome_tarefa = input("Digite o novo nome da tarefa que deseja atualizar: ")
        atualizar_nome_tarefa(tarefas, int(indice_tarefa), nome_tarefa)
    elif int(escolha) == 4:
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa que deseja marcar como completa: ")
        completar_tarefa(tarefas, int(indice_tarefa))
    elif int(escolha) == 5:
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif int(escolha) == 6:
        break

print("Programa finalizado")