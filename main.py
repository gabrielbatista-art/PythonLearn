'''
Projeto de aplicativo de todo em python
Gabriel Batista
'''

import datetime
from Tarefa import Tarefa
from Utils import adicionarTarefa, listaComandos, comandoHandler

tarefas : list = []
comandos : list = ["Add Tarefa", "Listar Tarefas", "Ver Tarefa", "Finalizar Tarefa", "Excluir Tarefa", "Sair"]
comando : int = 0


while comando != 6:
    print("-------- TODO PY ---------")
    listaComandos(comandos)
    comando = int(input("O que deseja fazer? "))
    comandoHandler(comando, comandos, tarefas)
