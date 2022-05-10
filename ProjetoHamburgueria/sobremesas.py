import conta
import this
import cardapio
import operacoes

this.opcaoSobremesas = 0
def cardapioSobremesa():
    operacoes.selecionarSobremesa()
    this.opcaoSobremesas = int(input('Opção selecionada: '))  # Coletando a sobremesa selecionado

def selecionarSobremesas():
    try:
        while this.opcaoSobremesas != 7:
            cardapioSobremesa()
            if this.opcaoSobremesas == 1:
                print('____________________________________________')
                print('\nVocê adicionou Torta Gelada Negresco ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(64.90, 'Torta gelada Negresco')

            elif this.opcaoSobremesas == 2:
                print('____________________________________________')
                print('\nVocê adicionou Torta Gelada Maracuja ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(64.90, 'Torta gelada de Maracuja')


            elif this.opcaoSobremesas == 3:
                print('____________________________________________')
                print('\nVocê adicionou Mousse ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(59.00, "Mousse")

            elif this.opcaoSobremesas == 4:
                print('____________________________________________')
                print('\nVocê adicionou Cheesecake Gelado ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(69.00, 'Chessecake Gelado')

            elif this.opcaoSobremesas == 5:
                print('____________________________________________')
                print('\nVocê adicionou Sobremesa de Amendoim ao seu pedido\n')
                print('____________________________________________')
                conta.calculoValor(52.00, 'Sobremesa de Amendoim')

            elif this.opcaoSobremesas == 6:
                cardapio.redirecionarCardapio()

            else:
                print('____________________________________________')
                print('\nSelecione uma opção válida\n')
                print('____________________________________________')
    except:
        print('____________________________________________')
        print('\nSelecione uma opção válida\n')
        print('____________________________________________')
        selecionarSobremesas()