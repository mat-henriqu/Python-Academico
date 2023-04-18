def imprimir_resultado(numero, resultado):
    mensagem = f'O numero {numero} nao é primo'
    if resultado:
        mensagem = f'O numero {numero} é primo'
    return mensagem
