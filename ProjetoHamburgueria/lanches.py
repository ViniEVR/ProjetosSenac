import conta
import this
import cardapio
import operacoes

this.opcaoLanches = 0
def cardapioLanches():
    operacoes.selecionarLanche()
    this.opcaoLanches = int(input('Opção selecionada: '))  # Coletando o lanche selecionado

def selecionarLanches():
    try:
        while this.opcaoLanches != 11:
            cardapioLanches()
            if this.opcaoLanches == 1:
                print('____________________________________________')
                print('\nVocê adicionou Holly Fantástico ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(39.90, 'Holly Fantástico')

            elif this.opcaoLanches == 2:
                print('____________________________________________')
                print('\nVocê adicionou Pulp Ficton Vincent ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(6.90, 'Pulp Fiction Vincent')


            elif this.opcaoLanches == 3:
                print('____________________________________________')
                print('\nVocê adicionou Pulp Fiction Jules ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(29.90, 'Pulp Fiction Jules')

            elif this.opcaoLanches == 4:
                print('____________________________________________')
                print('\nVocê adicionou Holly Smoked Jam ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(36.90, 'Holly Smoked Jam')

            elif this.opcaoLanches == 5:
                print('____________________________________________')
                print('\nVocê adicionou Holly Salad ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(28.90, 'Holly Salad')

            elif this.opcaoLanches == 6:
                print('____________________________________________')
                print('\nVocê adicionou Holly Cheese ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(24.90, 'Holly Cheese')

            elif this.opcaoLanches == 7:
                print('____________________________________________')
                print('\nVocê adicionou Holly Bacon ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(29.90, 'Holly Bacon')

            elif this.opcaoLanches == 8:
                print('____________________________________________')
                print('\nVocê adicionou Hulk ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(29.90, 'Hulk')

            elif this.opcaoLanches == 9:
                print('____________________________________________')
                print('\nVocê adicionou King Kong ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(47.90, 'King Kong')

            elif this.opcaoLanches == 10:
                print('____________________________________________')
                print('\nVocê adicionou Kill Bill ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(39.90, 'Kill Bill')

            elif this.opcaoLanches == 11:
                cardapio.redirecionarCardapio()

            else:
                print('____________________________________________')
                print('\nSelecione uma opção válida\n')
                print('____________________________________________')
                selecionarLanches()
    except:
        print('____________________________________________')
        print('\nSelecione uma opção válida\n')
        print('____________________________________________')
        selecionarLanches()
