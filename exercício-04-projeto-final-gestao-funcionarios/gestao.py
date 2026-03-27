def cadastrar_funcionario(id):
    """Função responsável por realizar o cadastro do funcionário em nosso dicionário global."""
    print('')
    print('-' * 50)
    print('-' * 11 + ' MENU CADASTRAR FUNCIONÁRIO ' + '-' * 11)


    # Dicionário temporário para adicionar as informações
    # referentes ao funcionário
    funcionario = {}


    nome = input('Por favor entre com o nome do Funcionário: ').lower()
    setor = input('Por favor entre com o setor do Funcionário: ').lower()


    funcionario['id'] = id
    funcionario['nome'] = nome
    funcionario['setor'] = setor


    # Tratamento referente ao salário que será digitado
    # pelo usuário
    while True:
        try:
            salario = float(input('Por favor entre com o salário do Funcionário: '))
            funcionario['salario'] = salario
            break
        except ValueError:
            print('A entrada não representa um número válido.')


    # Adicionando o dicionário temporário em nossa
    # lista de funcionários
    lista_funcionarios.append(funcionario.copy())


    # Mensagem que confirma a inserção do funcionário
    # no sistema
    print('\nFuncionário cadastrado com sucesso.')
    print('Retornando ao menu principal...\n')




def consultar_funcionario():
    """Função responsável por realizar a consulta dos funcionários
    em nosso sistema."""
    while True:
        print('')
        print('-' * 50)
        print('-' * 11 + ' MENU CONSULTAR FUNCIONÁRIO ' + '-' * 11)
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos os Funcionários')
        print('2 - Consultar Funcionários por id')
        print('3 - Consultar Funcionário(s) por setor')
        print('4 - Retornar ao menu')


        opcao = input('>> ')


        # Realiza a validação da opção digitada pelo usuário
        while opcao not in ['1', '2', '3', '4']:
            print('Opção inválida. Digite novamente.')
            opcao = input('>>')


        print('-' * 17)


        if opcao == '1':
            for funcionario in lista_funcionarios:
                # Realiza a impressão das informações de todos
                # os funcionários cadastrados
                for key, value in funcionario.items():
                    if key == 'id':
                        print(f'{key}: {value}')
                    elif key == 'salario':
                        print(f'{key}: R${value:.2f}')
                    else:
                        print(f'{key}: {value.capitalize()}')
                print('')


            print('-' * 17)
        elif opcao == '2':


            # Realiza o tratamento do número referente ao id
            # que será digitado pelo usuário
            while True:
                try:
                    id_func = int(input('Informe o id do funcionário: '))
                    break
                except ValueError:
                    print('Id inválido. Por favor, digite novamente.\n')


            for funcionario in lista_funcionarios:
                # Caso o id do funcionário seja encontrado em sistema,
                # serão realizadas as impressões de suas informações
                if id_func in funcionario.values():
                    print('Funcionário localizado.\n')


                    for key, value in funcionario.items():
                        if key == 'id':
                            print(f'{key}: {value}')
                        elif key == 'salario':
                            print(f'{key}: R${value:.2f}')
                        else:
                            print(f'{key}: {value.capitalize()}')
                break


        elif opcao == '3':
            setor = input('Por favor, informe o nome do setor do funcionário: ').lower()


            print('')


            for funcionario in lista_funcionarios:
                # Caso seja encontrado funcionário com o setor digitado,
                # serão realizadas as impressões de seus dados.
                if setor in funcionario.values():
                    for key, value in funcionario.items():
                        if key == 'id':
                            print(f'{key}: {value}')
                        elif key == 'salario':
                            print(f'{key}: R${value:.2f}')
                        else:
                            print(f'{key}: {value.capitalize()}')
                    print('')


        elif opcao == '4':
            # volta ao menu principal
            return




def remover_funcionario():
    """Função responsável por remover o funcionário através da inserção
    de seu id."""
    print('')
    print('-' * 50)
    print('-' * 11 + ' MENU REMOVER FUNCIONÁRIO ' + '-' * 11)


    # Caso não seja digitado id referente a algum funcionário já
    # cadastrado, a inserção do dado será solicitada novamente
    while True:
        try:
            id_func = int(input('Informe o id do funcionário: '))


            funcionario_encontrado = False


            for funcionario in lista_funcionarios:
                if id_func in funcionario.values():
                    funcionario_encontrado = True


            # Caso não seja encontrado funcionário,
            # será executada essa sequência de código
            if not funcionario_encontrado:
                print('Id inválido. Id não corresponde a um funcionário da lista.\n')
                continue
            break
        # Caso o usuário digite um valor inválido na conversão para int,
        # será executada a seguinte sequência de código
        except ValueError:
            print('Id inválido. Por favor, digite o id novamente.\n')


    # Código responsável por realizar a exclusão do funcionário
    # com o id digitado
    for index, funcionario in enumerate(lista_funcionarios):
        if id_func in funcionario.values():
            lista_funcionarios.pop(index)


    print('Funcionário excluído com sucesso.')
    print('Retornando ao menu principal...')


# Início do programa principal
print('Bem vindo a Empresa do Jhonata Samuel')


# Declaracão de variáveis iniciais
lista_funcionarios = []
id_global = 5093688


# Loop de execução do programa
while True:
    print('')
    print('-' * 50)
    print('-' * 17 + ' MENU PRINCIPAL ' + '-' * 17)


    print('Escolha a opção desejada:')
    print('1 - Cadastrar Funcionários')
    print('2 - Consultar Funcionário(s)')
    print('3 - Remover Funcionário')
    print('4 - Sair')


    opcao = input('>> ')


    if opcao == '1':
        cadastrar_funcionario(id_global)
        id_global += 1
    elif opcao == '2':
        consultar_funcionario()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        # Finaliza a execução do programa principal
        print('\nEncerrando o programa...')
        break
    else:
        print('Opção inválida.\n')
