from exercicios.tema4.modulo3.exemploHerança.classeMae import ClasseSomaMultiplica


class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a-self.b

    def dividir(self):
        return self.a/self.b
