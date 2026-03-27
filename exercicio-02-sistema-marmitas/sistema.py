# inicialização de variaveis
listaDePedidos = []
numeroDoPedido = 1
nomesSabor = {
    'BA': 'Bife Acebolado',
    'FF': 'Filé de Frango'
}

# Mensagem de boas-vindas
print('-' * 6 + ' Bem-vindo a Loja de Marmitas do Jhonata Samuel ' + '-' * 6)
print('-' * 26 + 'Cardápio' + '-' * 26)
print('-' * 60)
print('---' + '| Tamanho | Bife Acebolado (BA) | Filé de Frango(FF) |' + '---')
print('---' + '|    P    |      R$ 16.00       |      R$ 15.00      |' + '---')
print('---' + '|    M    |      R$ 18.00       |      R$ 17.00      |' + '---')
print('---' + '|    G    |      R$ 22.00       |      R$ 21.00      |' + '---')
print('-' * 60)


while True:
    # Inicialização de variáveis
    sabor = ''
    tamanho = ''

    # Código responsável por solicitar e validar o sabor
    # e tamanho do prato
    while True:
        sabor = input('Entre com o sabor desejado (BA/FF): ').upper()
        if sabor not in ['BA', 'FF']:
            print('Sabor inválido. Tente novamente\n')
            continue

        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
        if tamanho not in ['P', 'M', 'G']:
            print('Tamanho inválido. Tente novamente\n')
            continue
        break

    valorPrato = 0

    # código responsável por definir o valor do prato
    # seguindo as regras de negócio
    if sabor == 'BA':
        if tamanho == 'P':
            valorPrato = 16.00
        elif tamanho == 'M':
            valorPrato = 18.00
        else:
            valorPrato = 22.00
    elif sabor == 'FF':
        if tamanho == 'P':
            valorPrato = 15.00
        elif tamanho == 'M':
            valorPrato = 17.00
        else:
            valorPrato = 21.00

    # realiza a adicão do número do pedido e valor do prato à lista de pedidos
    listaDePedidos.append({
        'numeroDoPedido': numeroDoPedido,
        'valorPrato': valorPrato
    })

    print(f'Você pediu um {nomesSabor[sabor]} no tamanho {tamanho}: R$ {valorPrato:.2f}')

    # codigo responsável por confirmar e validar a opção de adição de outro pedido
    desejaOutroPedido = input('\nDeseja pedir mais alguma coisa? (S/N): ').upper()

    while desejaOutroPedido not in ['S', 'N']:
        print('Opção inválida. Tente novamente\n')
        desejaOutroPedido = input('Deseja pedir mais alguma coisa? (S/N): ').upper()

    # define o encerramento ou não do programa segundo a escolha de adição de outro pedido
    if desejaOutroPedido == 'S':
        numeroDoPedido += 1
        continue
    elif desejaOutroPedido == 'N':
        break


# variável acumuladora
total = 0

# realiza o calculo do total a pagar
for pedido in listaDePedidos:
    total += pedido['valorPrato']

print(f'\nO valor total a ser pago: R$ {total:.2f}')
