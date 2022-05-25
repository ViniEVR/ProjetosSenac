import this

import cardapio
import operacoes
import lanches

this.opcaoFuncionario = 0

def logar():
    this.codigo = 0
    this.senha = 0
    this.codigo = input('Digite o código: ')
    this.senha = input('Digite a senha: ')

    if this.codigo == "1" and this.senha == "1":
        menuFuncionario()
    else:
        print('\nDigite um código ou senha válidos.\n')
        print('Ou então selecione um item do menu: \n\n')

def mostrarMenu():
    print('\n\n\n1.Cadastrar lanche\n'
          '2.Excluir lanche\n'
          '3.Cadastrar bebida\n'
          '4.Excluir bebida\n'
          '5.Cadastrar sobremesa\n'
          '6.Excluir sobremesa\n'
          '7.Cadastrar funcionário\n'
          '8.Retornar ao menu anterior')
    this.opcaoFuncionario = int(input('Opção selecionada: '))

def menuFuncionario():
    try:
        this.opcaoFuncionario = 0
        while this.opcaoFuncionario != 8:
            mostrarMenu()
            if this.opcaoFuncionario == 1:
                nome = input('Digite o nome do lanche: ')
                ingredientes = input('\nDigite os ingredientes: ')
                preco = int(input('\nDigite o valor: R$'))

                operacoes.inserirLanches(nome, ingredientes, preco)

            elif this.opcaoFuncionario == 2:
                operacoes.selecionarLanche()
                this.codigo = int(input('Digite o número do lanche a ser deletado: '))

                operacoes.excluirLanche(this.codigo)

            elif this.opcaoFuncionario == 3:
                nome = input('Digite o nome da bebida: ')
                preco = int(input('Digite o valor: R$'))

                operacoes.inserirBebidas(nome, preco)

            elif this.opcaoFuncionario == 4:
                operacoes.selecionarBebida()
                this.codigo = int(input('Digite o número da bebida a ser deletado: '))

                operacoes.excluirBebida(this.codigo)

            elif this.opcaoFuncionario == 5:
                nome = input('Digite o nome da sobremesa: ')
                ingredientes = input('\nDigite os ingredientes: ')
                preco = int(input('\nDigite o valor: R$'))

                operacoes.inserirSobremesas(nome, ingredientes, preco)

            elif this.opcaoFuncionario == 6:
                operacoes.selecionarBebida()
                this.codigo = int(input('Digite o número da sobremesa a ser deletado: '))


            elif this.opcaoFuncionario == 7:
                print('Digite o nome: ')
                nome = input()
                print('Digite a senha: ')
                senha = input()
                operacoes.inserirFuncionario(nome, senha)

            elif this.opcaoFuncionario == 8:
                print('\n\n\n')
                cardapio.redirecionarCardapio()

            else:
                print('____________________________________________')
                print('\nSelecione uma opção válida\n')
                print('____________________________________________')
                menuFuncionario()
    except:
        print('____________________________________________')
        print('\nSelecione uma opção válida\n')
        print('____________________________________________')
        menuFuncionario()



