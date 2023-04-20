from exercicios.tema4.modulo2.exemploAgregacao.empregado import Empregado
from exercicios.tema4.modulo2.exemploAgregacao.salario import Salario

salario = Salario(10000, 700)
empregado = Empregado('Matheus', 46, salario)
print(empregado.salario_total())
