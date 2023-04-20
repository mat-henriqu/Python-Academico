from exercicios.tema4.modulo1.exercicio1mod1.pessoaPOO import Pessoa

pessoa1 = Pessoa("Matheus", "Brasil")
pessoa2 = Pessoa("Patricia", "Brasil")

print(f'Filho \n Nome: {pessoa1.get_nome()} \n Endereço: {pessoa1.get_ender()}')
print(f'Mãe \n Nome: {pessoa2.get_nome()} \n Endereço: {pessoa2.get_ender()}')
