import datetime as date

class Tarefa():
    def __init__(self, titulo : str, descricao : str):
        self.titulo : str = titulo
        self.descricao : str = descricao
        self.finalizacao : date
        self.criacao : date = date.datetime.now()
        self.finalizada : bool = False


    #Métodos
    def statusTarefa(self):
        print(
            "---- DETALHES TAREFA ----\n"
            f"Título: {self.getTitulo()}\n"
            f"Descricao: {self.getDescricao()}\n"
            f"Finalizada: {self.getFinalizada()}"
        )

    def finalizarTarefa(self):
        datenow = date.datetime.now()

        if not self.finalizada:
            self.setFinalizacao(datenow)
            self.setFinalizada(True)
        else:
            print("Tarefa Finalizada")





    
    #Getters e setters
    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo
    
    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao
    
    def getFinalizacao(self):
        return self.finalizacao

    def setFinalizacao(self, data : date):
        self.finalizacao = data

    def getFinalizada(self):
        return self.finalizada
    
    def setFinalizada(self, status : bool):
        self.finalizada = status
