import conta
import this
import cardapio

this.opcaoSobremesas = 0
def cardapioSobremesas():
    print('Escolha a sobremesa que deseja!\n' +
          '\n\n\n1.Torta Gelada Negresco R$ 64,90\n ingredientes: Torta gelada com base de bolacha Negresco e mousse de maracujá. Manter refrigerado.' +
          '\n\n\n2.Torta Gelada Maracuja R$ 64,90\n ingredientes: Torta gelada com base de pão de ló ou casquinha de bolacha com recheio a base de maracujá, creme de leite e leite condensado. Manter refrigerado.' +
          '\n\n\n3.Mousse Sabores R$ 59,00\n ingredientes: Escolha entre os sabores chocolate, maracujá, morango ou napolitano (chocolate, morango e baunilha). Manter refrigerado.' +
          '\n\n\n4.Cheesecake Gelado R$ 69,00\n ingredientes: Sobremesa com base de bolacha e recheio composto de cream cheese e leite condensado, com cobertura de frutas vermelha.' +
          '\n\n\n5.Sobremesa de Amendoim R$ 52,00\n ingredientes: Sobremesa cremosa composta de amendoim, açúcar, manteiga e creme de leite. +'
          '\n\n\n6.Retornar ao cardápio principal ')
    this.opcaoSobremesas = int(input('Opção selecionada:'))  # Coletar a digitação do usuário

def selecionarSobremesas():
    try:
        while this.opcaoSobremesas != 7:
            cardapioSobremesas()
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