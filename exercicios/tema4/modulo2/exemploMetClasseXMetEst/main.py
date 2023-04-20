from exercicios.tema4.modulo2.exemploMetClasseXMetEst.pessoa import Pessoa

pessoa1 = Pessoa('Matheus', 26)
pessoa2 = Pessoa.apartirAnoNascimento('Henrique', 2001)
print(f'Nome: {pessoa1.nome} \nIdade: {pessoa1.idade}')
print(f'Nome: {pessoa2.nome} \nIdade: {pessoa2.idade}')
print(f'É maior de idade: {Pessoa.ehMaiorIdade(21)}')
