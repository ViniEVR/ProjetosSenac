import this
import operacoes
import lanches

this.opcaoFuncionario = 0

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

def menu():
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



