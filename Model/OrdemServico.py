class OrdemServico:
    def __init__(self, idordemservico, idveiculo, prazo, defeito, valortotal):
        self.idordemservico = idordemservico
        self.idveiculo = idveiculo
        self.prazo = prazo
        self.defeito = defeito
        self.valortotal = valortotal


    def __str__(self):
        return self.defeito