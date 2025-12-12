class Cliente:
    def __init__(self, idcliente, nome, endereco, telefone):
        self.idcliente = idcliente
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone


    def __str__(self):
        return self.nome