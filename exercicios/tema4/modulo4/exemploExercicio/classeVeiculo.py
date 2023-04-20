class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro

    def toStr(self):
        print(f'Nome: {self.nome}')
        print(f'Velocidade maxima: {self.velocidade_max}')
        print(f'Quilometro por litro: {self.quilometro_litro}')

