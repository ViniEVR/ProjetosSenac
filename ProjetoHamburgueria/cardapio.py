import this

this.opcao = 0
def mostrarCardapio():
    print('1. Lanches\n' +
          '2. Bebidas\n' +
          '3. Sobremesas\n' +
          '4. Pagar a conta e sair\n')

    this.opcao = int(input('Opção selecionada: '))#Coletando opçao do usuario

def redirecionarCardapio():
    while this.opcao != 4:
        mostrarCardapio()
        if this.opcao == 1:
            print('1 né')

        if this.opcao == 2:
            print('2 né')

        if this.opcao == 3:
            print('3 né')

        if this.opcao == 4:
            print('4 né')
        else:
            print('____________________________________________')
            print('\nSelecione uma opção válida\n')
            print('____________________________________________')
            redirecionarCardapio()