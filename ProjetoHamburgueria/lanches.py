import conta
import this
import cardapio
import operacoes

this.opcaoLanche = 0

def cardapioLanches():
    operacoes.selecionarLanche()
    print('-1 Voltar ao cardápio\n')

    this.opcaoLanche = int(input('Opção selecionada: '))  # Coletando o lanche selecionado

def selecionarLanches():
    try:
        cardapioLanches()
        operacoes.contaLanche(this.opcaoLanche)


    except:
        print('____________________________________________')
        print('\nSelecione uma opção válida\n')
        print('____________________________________________')
        selecionarLanches()
