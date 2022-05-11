import conta
import this
import cardapio
import operacoes

this.opcaoSobremesa = 0

def cardapioSobremesas():
    operacoes.selecionarSobremesa()
    print('-1 Voltar ao cardápio\n')
    this.opcaoSobremesa = int(input('Opção selecionada: '))  # Coletando a sobremesa selecionado

def selecionarSobremesas():
    try:
        cardapioSobremesas()
        operacoes.contaSobremesa(this.opcaoSobremesa)


    except:
        print('____________________________________________')
        print('\nSelecione uma opção válida\n')
        print('____________________________________________')
        selecionarSobremesas()

