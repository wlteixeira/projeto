from Model.Cliente import Cliente

SQL_SELECT_CLIENTE = 'SELECT * FROM cliente'
SQL_SELECT_CLIENTE_ID = 'SELECT * FROM cliente WHERE idcliente = %s'
SQL_INSERT_CLIENTE = 'INSERT INTO cliente (nome, endereco, telefone) VALUES (%s, %s, %s)'
SQL_DELETE_CLIENTE = 'DELETE FROM cliente WHERE idcliente = %s'
SQL_UPDATE_CLIENTE = ('UPDATE cliente SET nome = %s, endereco = %s, telefone = %s WHERE idcliente = %s')


class ClienteDao:
    def __init__(self, conn):
        self.__db = conn


    def salvar(self, cliente):
        cursor = self.__db.connection.cursor()
        if cliente.idcliente is None:
            cursor.execute(SQL_INSERT_CLIENTE, (cliente.nome, cliente.endereco, cliente.telefone))
            cliente.idcliente = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_CLIENTE, (cliente.nome, cliente.endereco, cliente.telefone, cliente.idcliente))

        
        self.__db.connection.commit()
        return cliente


    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CLIENTE)
        tuplas = cursor.fetchall()
        lista_clientes = self.traduz_clientes(tuplas)
        return lista_clientes


    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CLIENTE_ID, (id,))
        tupla = cursor.fetchone()
        cliente = self.traduz_cliente(tupla)
        return cliente


    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_CLIENTE, (id,))
        self.__db.connection.commit()

    def traduz_cliente(self, tupla):
        cliente = Cliente(tupla[0], tupla[1], tupla[2], tupla[3])
        return cliente
    
    def traduz_clientes(self, tuplas):
        lista_clientes =[]
        for t in tuplas:
            cliente = self.traduz_cliente(t)
            lista_clientes.append(cliente)
        return lista_clientes