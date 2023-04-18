# F(x)= ax²+bx+c
from exercicios.tema3.modulo3.exemplodelta.calculando import calcular_raizes
from exercicios.tema3.modulo3.exemplodelta.dados import entrada_dados
from exercicios.tema3.modulo3.exemplodelta.delta import calc_delta

print('Coeficiente A')
a = entrada_dados()

print('Coeficiente B')
b = entrada_dados()

print('Coeficiente C')
c = entrada_dados()

delta = calc_delta(a, b, c)

resultado = calcular_raizes(a, b, c, delta)

print(resultado)
