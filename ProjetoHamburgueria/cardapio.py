import this
import conta
import bebidas
import lanches
import sobremesas

this.opcaoCardapio = 0
def mostrarCardapio():
    print('1. Lanches\n' +
          '2. Bebidas\n' +
          '3. Sobremesas\n' +
          '4. Pagar a conta e sair\n')

    this.opcaoCardapio = int(input('Opção selecionada: '))#Coletando opçao do usuario

def redirecionarCardapio():
    try:
        while this.opcaoCardapio != 4:
            mostrarCardapio()

            if this.opcaoCardapio == 1:
                print(lanches.selecionarLanches())

            elif this.opcaoCardapio == 2:
                print(bebidas.selecionarBebida())

            elif this.opcaoCardapio == 3:
                print(sobremesas.selecionarSobremesas())

            elif this.opcaoCardapio == 4:
                print(conta.contaComItens())

            else:
                print('____________________________________________')
                print('\nSelecione uma opção válida\n')
                print('____________________________________________')
                redirecionarCardapio()
    except:
        print('____________________________________________')
        print('\nSelecione uma opção válida\n')
        print('____________________________________________')
        redirecionarCardapio()