from Model.Veiculo import Veiculo

SQL_SELECT_VEICULO = 'SELECT * FROM veiculo'
SQL_INSERT_VEICULO = 'INSERT INTO veiculo (idcliente, marca, modelo, ano) VALUES (%s, %s, %s, %s)'
SQL_DELETE_VEICULO = 'DELETE FROM veiculo WHERE idveiculo = %s'
SQL_SELECT_VEICULO_ID = 'SELECT * FROM veiculo WHERE idveiculo = %s'
SQL_UPDATE_VEICULO = ('UPDATE veiculo SET idcliente = %s, marca = %s, modelo = %s, ano = %s WHERE idveiculo = %s')


class VeiculoDao:
    def __init__(self, conn):
        self.__db = conn


    def salvar(self, v):
        cursor = self.__db.connection.cursor()
        if not v.idveiculo:
            cursor.execute(SQL_INSERT_VEICULO, (v.idcliente, v.marca, v.modelo, v.ano))
            v.idveiculo = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_VEICULO, (v.idcliente, v.marca, v.modelo, v.ano, v.idveiculo))
        
        self.__db.connection.commit()
        return v


    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_VEICULO)
        lista = cursor.fetchall()
        lista_veiculos = self.traduz_veiculos(lista)
        return lista_veiculos


    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_VEICULO_ID, (id,))
        tupla = cursor.fetchone()
        veiculo = self.traduz_veiculo(tupla)
        return veiculo


    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_VEICULO, (id,))
        self.__db.connection.commit()

    def traduz_veiculo(self, tupla):
        v = Veiculo(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
        return v
    
    def traduz_veiculos(self, tuplas):
        lista_veiculos =[]
        for t in tuplas:
            veiculo = self.traduz_veiculo(t)
            lista_veiculos.append(veiculo)
        return lista_veiculos