from exercicios.tema3.modulo2.exercicio2mod2.fatorialIterativo import fatorial_iterativo
from exercicios.tema3.modulo2.exercicio2mod2.fatorialRecursivo import fatorial_recursivo

numero = int(input("Digite um numero para calcular o fatorial"))
print(f'O fatorial de {numero} é: {fatorial_iterativo(numero)}')
print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')
