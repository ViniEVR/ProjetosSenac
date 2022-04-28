import this
import conta
import bebidas

this.opcaoCardapio = 0
def mostrarCardapio():
    print('1. Lanches\n' +
          '2. Bebidas\n' +
          '3. Sobremesas\n' +
          '4. Pagar a conta e sair\n')

    this.opcaoCardapio = int(input('Opção selecionada: '))#Coletando opçao do usuario

def redirecionarCardapio():
    while this.opcaoCardapio != 90:
        print('____________________________________________')
        print('\nValor da conta até o momento\nR$:' + str(conta.calculoValor(0)))
        print('____________________________________________')
        mostrarCardapio()

        if this.opcaoCardapio == 1:
            print('1 né')

        elif this.opcaoCardapio == 2:
            print(bebidas.selecionarBebida())

        elif this.opcaoCardapio == 3:
            print('É 3 né')

        elif this.opcaoCardapio == 4:
            print('4 né')

        else:
            print('____________________________________________')
            print('\nSelecione uma opção válida\n')
            print('____________________________________________')
            redirecionarCardapio()