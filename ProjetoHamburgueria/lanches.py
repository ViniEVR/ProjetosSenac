import conta
import this
import cardapio

this.opcaoLanches = 0
def cardapioLanches():
    print('Escolha o Hamburguer que deseja!\n' +
          '\n\n\n1. Holly Fantástico R$ 39,90\n ingredientes: Pão brioche + burger 180g + rúcula + creme de gorgonzola + bacon bits + maionese defumada.  ' +
          '\n\n\n2. Pulp Ficton Vincent R$ 26,90\n ingredientes: Pão, burger de 150g, american cheese, ketchup, mostarda, cebola branca e picles.   ' +
          '\n\n\n3. Pulp Fiction Jules R$ 29,90\n ingredientes: Pão brioche, burger de 150g, cheddar e cebola caramelizada - acompanha maionese clássica.  ' +
          '\n\n\n4. Holly Smoked Jam R$ 36,90\n ingredientes: Pão brioche, burger de 180g, queijo Gouda, maionese defumada, geléia de bacon apimentada.    ' +
          '\n\n\n5. Holly Salad R$ 28,90\n ingredientes: Pão brioche + burger de 150g + american cheese + alface + tomate + cebola roxa - acompanha maionese verde.  ' +
          '\n\n\n6. Holly Cheese R$ 24,90\n ingredientes: Pão brioche + burger 150g + american cheese - acompanha maionese verde.   ' +
          '\n\n\n7. Holly Bacon R$ 29,90\n ingredientes: Pão brioche + burger 150g + american cheese + bacon caramelizado.   ' +
          '\n\n\n8. Hulk R$ 29,90\n ingredientes: Pão brioche, double smashburger de 150g, cheddar, rúcula, cebola caramelizada e picles.   ' +
          '\n\n\n9. King Kong R$ 47,90\n ingredientes: Pão, 2 burgers de 180g, american cheese, alface, tomate, cebola roxa, bacon e acompanha maionese de tabasco.    ' +
          '\n\n\n10. Kill Bill R$ 39,90\n ingredientes: Pão brioche + burger 180g + cheddar cremoso e bacon bits, o cheddar e o bacon vão separados pra vc colocar como desejar.   ' +
          '\n\n\n11.Retornar ao cardápio principal')
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
