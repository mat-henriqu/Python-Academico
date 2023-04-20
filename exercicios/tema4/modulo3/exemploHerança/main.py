from exercicios.tema4.modulo3.exemploHerança.classeDerivada import Derivada

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero'))

d = Derivada(numero1, numero2)
print(f'A soma desses dois numeros é: {d.somar()}')
print(f'A subtração desses dois numeros é: {d.subtrair()}')
print(f'A divisão desses dois numeros é: {d.dividir()}')
print(f'A multiplicação desses dois numeros é: {d.multipiplicar()}')
