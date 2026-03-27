def validar_num(mensagem, formato):
    """Função responsável por validar a entrada do número e converter para o formato
    desejado (int ou float)."""

    # Loop responsável por validar o tipo digitado e retornar ao programa principal
    while True:
        num = ''
        try:
            # Se o formato de dado solicitado a função for float,
            # será realizada a conversão para este tipo
            if formato == 'float':
                num = float(input(mensagem))
            elif formato == 'int':
                num = int(input(mensagem))

            if num > 0:
                # Caso o número seja positivo,
                # retorna ao programa inicial
                # o valor convertido para o formato solicitado
                return num
            else:
                print('\nO número digitado é negativo. Digite novamente.')

        # Realiza a exceção de erro, caso o valor digitado
        # pelo usuário não seja uma string válida para conversão
        except ValueError:
            print('\nNúmero invalido. Digite novamente.')


# Mensagem de boas-vindas
print('Bem-vindo a Loja do Jhonata Samuel')

# inicialização de váriáveis através do chamado à função validarNum
valorDoPedido = validar_num('Entre com o valor do pedido: ', 'float')
quantidadeParcelas = validar_num('Entre com a quantidade de parcelas: ', 'int')


# Implementação de juros conforme a quantidade de parcelas
if quantidadeParcelas >= 13:
    juros = 32 / 100
elif quantidadeParcelas >= 9:
    juros = 16 / 100
elif quantidadeParcelas >= 6:
    juros = 8 / 100
elif quantidadeParcelas >= 4:
    juros = 4 / 100
else:
    juros = 0


# Código responsável por calcular o valor das parcelas
# e o total a ser parcelado
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

# Apresenta ao usuário o valor da parcela e o total a parcelar
print(f'\nO valor das parcelas é de: R$ {valorDaParcela:.2f}')
print(f'O valor Total parcelado é de: R$ {valorTotalParcelado:.2f}')
