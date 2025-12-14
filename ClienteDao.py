from Model.Cliente import Cliente

SQL_SELECT_CLIENTE = 'SELECT * FROM cliente'
SQL_SELECT_CLIENTE_ID = 'SELECT * FROM cliente WHERE idcliente = %s'
SQL_INSERT_CLIENTE = 'INSERT INTO cliente (nome, endereco, telefone) VALUES (%s, %s, %s)'
SQL_UPDATE_CLIENTE = 'UPDATE cliente SET nome = %s, endereco = %s, telefone = %s WHERE idcliente = %s'
SQL_DELETE_CLIENTE = 'DELETE FROM cliente WHERE idcliente = %s'


class ClienteDao:
    def __init__(self, conn):
        self.__db = conn

    def salvar(self, cliente):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_INSERT_CLIENTE,(cliente.nome, cliente.endereco, cliente.telefone))
        self.__db.connection.commit()
        cliente.idcliente = cursor.lastrowid
        return cliente

    def atualizar(self, c):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_UPDATE_CLIENTE,(c.nome, c.endereco, c.telefone, c.idcliente))
        self.__db.connection.commit()

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CLIENTE)
        return self.traduz_clientes(cursor.fetchall())

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CLIENTE_ID, (id,))
        tupla = cursor.fetchone()

        if tupla:
            return self.traduz_cliente(tupla)
        return None

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_CLIENTE, (id,))
        self.__db.connection.commit()

    def traduz_cliente(self, t):
        return Cliente(t[0], t[1], t[2], t[3])

    def traduz_clientes(self, tuplas):
        return [self.traduz_cliente(t) for t in tuplas]
