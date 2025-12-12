from ClienteDao import Cliente

SQL_SELECT_CLIENTE = 'SELECT * FROM cliente'
SQL_SELECT_CLIENTE_ID = 'SELECT * FROM cliente WHERE idcliente = %s'
SQL_INSERT_CLIENTE = 'INSERT INTO cliente (idcliente, nome, endereco, telefone) VALUES (%s, %s, %s, %s)'
SQL_DELETE_CLIENTE = 'DELETE FROM cliente WHERE idcliente = %s'


class ClienteDao:
    def __init__(self, conn):
        self.__db = conn


def salvar(self, cliente):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_INSERT_CLIENTE, (cliente.idcliente, cliente.nome, cliente.endereco, cliente.telefone))
    self.__db.connection.commit()
    return cliente


def listar(self):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_SELECT_CLIENTE)
    tuplas = cursor.fetchall()
    return [Cliente(*t) for t in tuplas]


def listar_por_id(self, id):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_SELECT_CLIENTE_ID, (id,))
    tupla = cursor.fetchone()
    return Cliente(*tupla)


def deletar(self, id):
    cursor = self.__db.connection.cursor()
    cursor.execute(SQL_DELETE_CLIENTE, (id,))
    self.__db.connection.commit()