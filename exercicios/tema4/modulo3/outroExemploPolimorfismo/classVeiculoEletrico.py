from exercicios.tema4.modulo3.outroExemploPolimorfismo.classeVeiculo import Veiculo


class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print('Este veiculo utiliza eletricidade')
