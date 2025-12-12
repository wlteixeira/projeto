from OrdemServicoDao import OrdemServico

SQL_SELECT_OS = 'SELECT * FROM ordemservico'
SQL_SELECT_OS_ID = 'SELECT * FROM ordemservico WHERE idordemservico = %s'
SQL_INSERT_OS = 'INSERT INTO ordemservico VALUES (%s, %s, %s, %s, %s)'
SQL_DELETE_OS = 'DELETE FROM ordemservico WHERE idordemservico = %s'


class OrdemServicoDao:
    def __init__(self, conn):
        self.__db = conn


def salvar(self, os):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_INSERT_OS, (os.idordemservico, os.idveiculo, os.prazo, os.defeito, os.valortotal))
    self.__db.connection.commit()
    return os


def listar(self):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_SELECT_OS)
    return [OrdemServico(*t) for t in cursor.fetchall()]


def listar_por_id(self, id):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_SELECT_OS_ID, (id,))
    tupla = cursor.fetchone()
    return OrdemServico(*tupla)


def deletar(self, id):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_DELETE_OS, (id,))
    self.__db.connection.commit()