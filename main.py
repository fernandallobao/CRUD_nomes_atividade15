# Crie um CRUD de nomes. Ou seja, um programa que:
# - Cadastre um nome.
# - Pesquise pelos nomes cadastrados.
# - Altere um nome.
# - Delete um nome da lista.

# O usuário poderá inserir quantos nomes quiser.

lista_nomes = []

while True:
    print('\n\033[4m\033[35mEscolha uma opção: \033[0m')
    print('1 - Cadastrar um nome')
    print('2 - Pesquisar nomes')
    print('3 - Alterar um nome')
    print('4 - Deletar um nome')
    print('5 - Mostrar todos os nomes')
    print('6 - Sair')

    op = input(f'\033[32mDigite o índice da ação que deseja fazer: \033[0m')
    match op:
        case '1':
            nome = input('Informe um nome: ')
            lista_nomes.append(nome)
            print(f"Nome '{nome}' cadastrado com sucesso!")
        case '2':
            pes_nome = input('Informe o nome, ou parte dele, que deseja encontrar: ')
            if pes_nome in lista_nomes:
                print(f'{pes_nome} encontrado com sucesso!')
            else:
                print(f'{pes_nome} não encontrado!')
        case '3':
            antigo_nome = input('Informe o nome que deseja alterar: ')
            lista_nomes[lista_nomes.index(antigo_nome)] = input('Informe o novo nome: ')
            print(f'O nome {antigo_nome} foi alterado com sucesso!')
        case '4':
            del_nome = input('Informe o nome de deseja deletar: ')
            if del_nome in lista_nomes:
                lista_nomes.remove(del_nome)
                print(f'O nome {del_nome} foi deletado com sucesso!')
            else:
                print('Não foi possivel deletar!')
        case '5':
            print('\033[4m\033[33mEsta é a lista de nomes:\033[0m')
            for nome in lista_nomes:
                print(f'- {nome}')
        case '6':
            break

print('Progama encerrado!')
            
