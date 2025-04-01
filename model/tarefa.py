from model.database import Database
 
class Tarefa:
    def __init__(self, titulo, data_conclusao = None, id= None):
        self.titulo = titulo
        self.id = id
        self.data_conclusao = data_conclusao
 
    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados!?"""
        db = Database()
        db.conectar()
 
        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()
 
    def listarTarefa():
        """Retornar uma lista com todas as tarefas..."""
        db = Database()
        db.conectar()
 
        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
   
    @staticmethod
    def apagarTarefa(idTarefa):
        """Apaga uma tarefa cadastrada no banco de dados?"""
        db = Database()
        db.conectar()
        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (idTarefa,) # Precisa ser uma tupla!
        db.executar(sql, params)
        db.desconectar()
 
    def atualizarTarefa(self):
        db = Database()
        db.conectar()
        sql = "UPDATE tarefa SET titulo = %s, data_conclusao = %s WHERE id = %s"
        params = (self.titulo, self.data_conclusao, self.id)
        db.executar(sql, params)
        db.desconectar()
