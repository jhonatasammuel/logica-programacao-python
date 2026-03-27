# dicionario com o valor dos modelos
modelos = {
    'MCS': 1.8,
    'MLS': 2.1,
    'MCE': 2.9,
    'MLE': 3.2
}

# dicionario com o valor de cada opção de frete
fretes = {
    0: 0,
    1: 100,
    2: 200
}


def escolha_modelo():
    """Função responsável por solicitar o modelo desejado e retornar
    o respectivo custo."""

    modelo = ''

    while True:
        print('\nMCS - Manga Curta Simples')
        print('MLS - Manga Longa Simples')
        print('MCE - Manga Curta com Estampa')
        print('MLE- Manga Longa Com Estampa')

        modelo = input('\nEntre com o modelo desejado: ').upper()

        if modelo in ['MCS', 'MLS', 'MCE', 'MLE']:
            break

        print('Escolha inválida, entre com o modelo novamente')

    return modelos[modelo]


def num_camisetas():
    """Função responsável por solicitar a quantidade de camisetas e
    retornar a quantidade com a aplicação do desconto."""

    # loop responsável por validar a entrada do número de camisetas
    while True:
        try:
            num_camisetas = int(input('\nEntre com o número de camisetas: '))

        # tratamento de possível inserção inválida
        except ValueError:
            print('Entrada inválida.')
            print('Por favor, entre com o número de camisetas novamente.')
            continue

        if num_camisetas > 20000:
            # Caso solicitar acima de 20 mil camisetas, retorna para o início do loop
            print('Não aceitamos tantas camisetas de uma vez.')
            print('Por favor, entre com o número de camisetas novamente.')
            continue
        elif num_camisetas >= 2000:
            desconto = 12 / 100
        elif num_camisetas >= 200:
            desconto = 7 / 100
        elif num_camisetas >= 20:
            desconto = 5 / 100
        else:
            desconto = 0

        # retorna a quantidade de camisetas
        return num_camisetas * (1 - desconto)
def frete():
    """Função responsável por solicitar o tipo do frete e retornar
    o respectivo custo."""

    # loop responsável por validar a entrada do tipo de frete
    while True:
        print('\nTipos de frete:')
        print('1 - Frete por transportadora - R$ 100.00')
        print('2 - Frete por Sedex - R$ 200.00')
        print('0 - Retirar pedido na fábrica - R$ 0.00')

        try:
            frete = int(input('\nEscolha o tipo de frete: '))

            # Caso não seja o número respectivo ao frete
            # Retorna ao início do loop
            if frete not in [0, 1, 2]:
                print('Opção inexistente.')
                print('Por favor, escolha o tipo do frete novamente.')
                continue

        # tratamento de possível erro de inserção
        except ValueError:
            print('Entrada inválida.')
            print('Por favor, escolha o tipo do frete novamente.')
            continue

        # retorna o frete disposto no dicionário de fretes
        return fretes[frete]
# programa principal

print('Bem vindo a Frábrica de Camisetas do Jhonata Samuel')

modelo = escolha_modelo()
num_camisetas = int(num_camisetas())
frete = frete()

# calculo do total a ser pago
total = (modelo * num_camisetas) + frete

# mostra ao usuário informações pertinentes sobre compra
print(f'Total: R$ {total:.2f} (Modelo: {modelo:.2f} * Quantidade(com desconto): '
      f'{num_camisetas} + frete: R$ {frete:.2f})')
