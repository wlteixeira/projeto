class Veiculo:
    def __init__(self, idveiculo, idcliente, marca, modelo, ano):
        self.idveiculo = idveiculo
        self.idcliente = idcliente
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def __str__(self):
        return self.modelo