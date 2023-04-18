from exercicios.tema3.modulo2.exercicio1mod2.par import par


def somaPar(lista):
    soma = 0
    for num in lista:
        if par(num):
            soma = soma + num
    return soma
