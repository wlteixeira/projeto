from VeiculoDao import Veiculo

SQL_SELECT_VEICULO = 'SELECT * FROM veiculo'
SQL_INSERT_VEICULO = 'INSERT INTO veiculo VALUES (%s, %s, %s, %s, %s)'
SQL_DELETE_VEICULO = 'DELETE FROM veiculo WHERE idveiculo = %s'
SQL_SELECT_VEICULO_ID = 'SELECT * FROM veiculo WHERE idveiculo = %s'


class VeiculoDao:
    def __init__(self, conn):
        self.__db = conn


def salvar(self, v):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_INSERT_VEICULO, (v.idveiculo, v.idcliente, v.marca, v.modelo, v.ano))
    self.__db.connection.commit()
    return v


def listar(self):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_SELECT_VEICULO)
    lista = cursor.fetchall()
    return [Veiculo(*t) for t in lista]


def listar_por_id(self, id):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_SELECT_VEICULO_ID, (id,))
    tupla = cursor.fetchone()
    return Veiculo(*tupla)


def deletar(self, id):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_DELETE_VEICULO, (id,))
    self.__db.connection.commit()