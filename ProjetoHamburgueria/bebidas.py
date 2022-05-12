import conta
import this
import cardapio
import operacoes

this.opcaoBebida = 0

def cardapioBebidas():
    operacoes.selecionarBebida()
    print('-1 Voltar ao cardápio\n')

    this.opcaoBebida = int(input('Opção selecionada: '))  # Coletando a bebida selecionada

def selecionarBebidas():
    try:
        cardapioBebidas()
        operacoes.contaBebida(this.opcaoBebida)


    except:
        print('____________________________________________')
        print('\nSelecione uma opção válida\n')
        print('____________________________________________')
        selecionarBebidas()

