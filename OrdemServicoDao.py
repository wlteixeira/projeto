from Model.OrdemServico import OrdemServico

SQL_SELECT_OS = 'SELECT * FROM ordemservico'
SQL_SELECT_OS_ID = 'SELECT * FROM ordemservico WHERE idordemservico = %s'
SQL_INSERT_OS = 'INSERT INTO ordemservico (idveiculo, prazo, defeito, valortotal) VALUES (%s, %s, %s, %s)'
SQL_DELETE_OS = 'DELETE FROM ordemservico WHERE idordemservico = %s'
SQL_UPDATE_OS = ('UPDATE ordemservico SET idveiculo = %s, prazo = %s, defeito = %s, valortotal = %s WHERE idordemservico = %s')


class OrdemServicoDao:
    def __init__(self, conn):
        self.__db = conn


    def salvar(self, os):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_INSERT_OS, (os.idveiculo, os.prazo, os.defeito, os.valortotal))
        os.idordemservico = cursor.lastrowid
        self.__db.connection.commit()
        return os
    
    def atualizar(self, os):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_UPDATE_OS,(os.idveiculo, os.prazo, os.defeito, os.valortotal, os.idordemservico))
        self.__db.connection.commit()


    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_OS)
        tuplas = cursor.fetchall()
        lista_os = self.traduz_oss(tuplas)
        return lista_os


    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_OS_ID, (id,))
        tupla = cursor.fetchone()
        os = self.traduz_os(tupla)
        return os


    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_OS, (id,))
        self.__db.connection.commit()

    def traduz_os(self, tupla):
        os = OrdemServico(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
        return os
    
    def traduz_oss(self, tuplas):
        lista_oss =[]
        for t in tuplas:
            os = self.traduz_os(t)
            lista_oss.append(os)
        return lista_oss