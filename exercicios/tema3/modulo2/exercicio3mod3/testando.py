from exercicios.tema3.modulo2.exercicio3mod3.primo import e_primo
from exercicios.tema3.modulo2.exercicio3mod3.resultado import imprimir_resultado

numero = int(input("Digite um numero para testar se é primo: "))
resultado = e_primo(numero)
mensagem = imprimir_resultado(numero, resultado)
print(mensagem)
