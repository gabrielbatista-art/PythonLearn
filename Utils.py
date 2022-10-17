from Tarefa import Tarefa

def adicionarTarefa(titulo : str, descricao : str, lista : list):
    lista.append(Tarefa(titulo, descricao))


def listaComandos(lista):
    for comando in range(len(lista)):
        # print(comando)
        print(f"{[comando + 1]} {lista[comando]}")

def listaTarefas(lista):
    print("--- Lista De Tarefas ---")
    for tarefa in range(len(lista)):
        print(f"[{tarefa}] {lista[tarefa].titulo}")

def verTarefas(lista):
    for tarefa in lista:
        print(tarefa.titulo)

 
def comandoHandler(comando : int, comandos : list, lista : list):
    if comando == 1: #Adicionar
        titulo : str = str(input("Titulo da tarefa: "))
        descricao : str = str(input("Descricao da tarefa: "))

        lista.append(Tarefa(titulo, descricao))
        input("[Qualquer tecla para continuar.]")
    elif comando == 2: #Listar Tarefas
        listaTarefas(lista)

        input("[Qualquer tecla para continuar.]")
    elif comando == 3: #Ver Tarefa
        listaTarefas(lista)
        idtarefa : int = int(input("Qual Tarefa deseja olhar? "))

        lista[idtarefa].statusTarefa()
        input("[Qualquer tecla para continuar.]")

    elif comando == 4: #Finalizar Tarefa
        idtarefa : int = int(input("Qual Tarefa deseja finalizar? "))

        lista[idtarefa].finalizarTarefa()
        input("[Qualquer tecla para continuar.]")
    elif comando == 5: #Excluir Tarefa
        idtarefa : int = int(input("Qual Tarefa deseja excluir? "))

        excluido = lista.pop(idtarefa)
        print(f"Tarefa {excluido} foi removida com sucesso.")
        input("[Qualquer tecla para continuar.]")
    elif comando == 6:
        pass
