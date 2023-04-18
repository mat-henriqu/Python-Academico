import numpy as np


def calcular_raizes(a, b, c, delta):
    if delta < 0:
        resultado = 'A equação nao possui raizes nos numeros reais'
    elif delta == 0:
        x = -b / 2 * a
        resultado = f'A equação possui apenas a raiz {x}'
    else:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        resultado = f'A equação possui as raizes {x1} e {x2}'
    return resultado
