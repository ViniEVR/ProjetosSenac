import conta
import this
import cardapio

this.opcaoBebida = 0
def cardapioBebidas():
    print('\n\n1.Coca-cola R$ 7,90\n' +
          '2.Sprite R$ 6,90\n' +
          '3.Fanta uva R$ 6,90\n' +
          '4.Fanta laranja R$ 6,90\n' +
          '5.Suco de laranja R$ 8,90\n' +
          '6.Suco de maracuja R$ 8,90\n' +
          '7.Limonada R$ 8,90\n' +
          '8.Retornar ao cardápio principal')
    this.opcaoBebida = int(input('Opção selecionada: '))#Coletando a bebida selecionada

def selecionarBebida():
    try:
        while this.opcaoBebida != 8:
            cardapioBebidas()
            if this.opcaoBebida == 1:
                print('____________________________________________')
                print('\nVocê adicionou Coca-cola ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(7.90, "Coca-cola")

            elif this.opcaoBebida == 2:
                print('____________________________________________')
                print('\nVocê adicionou Sprite ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(6.90, "Sprite")


            elif this.opcaoBebida == 3:
                print('____________________________________________')
                print('\nVocê adicionou Fanta uva ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(6.90, "Fanta uva")

            elif this.opcaoBebida == 4:
                print('____________________________________________')
                print('\nVocê adicionou Fanta laranja ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(6.90, "Fanta laranja")

            elif this.opcaoBebida == 5:
                print('____________________________________________')
                print('\nVocê adicionou suco de laranja ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(8.90, "Suco de laranja")

            elif this.opcaoBebida == 6:
                print('____________________________________________')
                print('\nVocê adicionou suco de maracuja ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(8.90, "Suco de maracuja")

            elif this.opcaoBebida == 7:
                print('____________________________________________')
                print('\nVocê adicionou limonada ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(8.90, "Limonada")

            elif this.opcaoBebida == 8:
                cardapio.redirecionarCardapio()

            elif this.opcaoBebida == 9:
                conta.contaComItens()


            else:
                print('____________________________________________')
                print('\nSelecione uma opção válida\n')
                print('____________________________________________')
                selecionarBebida()
    except:
        print('____________________________________________')
        print('\nSelecione uma opção válida\n')
        print('____________________________________________')
        selecionarBebida()