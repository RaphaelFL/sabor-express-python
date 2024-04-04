import os

restaurantes = [{'nome': 'praça', 'categoria':'japonesa', 'ativo':False}, 
                {'nome': 'pizzaria', 'categoria':'italiana', 'ativo':True}]

def exbir_nome_do_sistema():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_menu():
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Alterar Status do Produto')
    print('4 - Sair do Sistema')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(f'\n{subtitulo}\n')
    print()

def cadastrar_produto():
    os.system('cls')
    print('Cadastrar de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    ativo = input('O restaurante está ativo? (s/n): ')
    ativo = True if ativo == 's' else False
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': ativo}
    restaurantes.append(dados_do_restaurante)
    print(f'Orestaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    retornar_menu()

def listar_restaurantes():
    os.system('cls')
    print('Listar restaurantes\n')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Sim' if restaurante['ativo'] else 'Não'
        print(f'{nome_restaurante} | {categoria_restaurante} | Ativo: {ativo}')
    
    retornar_menu()
    
def opcao_invalida():
    print('Opção Inválida!\n')
    retornar_menu()

def escolher_opcao(): 
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #print('Você escolheu a opção ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_produto()
        elif opcao_escolhida == 2:
            os.system('cls')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            os.system('cls')
            alterar_status_do_produto()
        elif opcao_escolhida == 4:
            os.system('cls')
            finalizar_app()
    except:
        os.system('cls')
        opcao_invalida()

def opcao_invalida():
    print('Opção Inválida!\n')
    retornar_menu()

def alterar_status_do_produto():
    exibir_subtitulo('Alterar status do produto')
    nome_restaurante = input('Digite o nome do restaurante: ')

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            print(f'O status do restaurante {nome_restaurante} foi alterado com sucesso!')
            ativo = input('O restaurante deve estar ativo? (s/n): ')
            ativo = True if ativo == 's' else False
            restaurante['ativo'] = ativo
            retornar_menu()
    if not nome_restaurante:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
        retornar_menu()


def retornar_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def main():
    exbir_nome_do_sistema()
    exibir_menu()
    escolher_opcao()
    finalizar_app()

if __name__ == '__main__':
    main()