import this
import sys

#Classe responsável por calcular o valor da conta
import cardapio

precoTotal = []
item = []
this.valorConta = 0


def calculoValor(precoItem, nomeItem):
    precoTotal.append(precoItem)
    item.append(nomeItem)
    this.valorConta = str(sum(precoTotal))
    calcularValorTotal()


def calcularValorTotal():
    print('____________________________________________')
    print('\nValor da conta até o momento \nR$:' + this.valorConta)
    print('____________________________________________')

def finalPrograma(opcao):
    if opcao == 1:
        print('Obrigado por comprar conosco!')

    elif opcao == 2:
        print('\n\n\n')
        cardapio.redirecionarCardapio()
    else:
        print('____________________________________________')
        print('\nDigite um valor válido\n')
        print('____________________________________________')
        contaComItens()

def contaComItens():
    try:
        j = 0
        for i in item:
            print(f"\n\n{i}, valor: R${precoTotal[j]}0")
            j += 1

        print('____________________________________________')
        print('\nValor da sua conta é de \nR$:' + this.valorConta)
        print('____________________________________________')
        opcao = int(input('1.Pagar \n' +
              '2.Voltar\n' +
                'Opcao selecionada: '           ))


        finalPrograma(opcao)


    except:
        j = 0
        for i in item:
            print(f"\n\n{i}, valor: R${precoTotal[j]}0")
            j += 1

        print('____________________________________________')
        print('\nValor da sua conta é de \nR$:' + this.valorConta)
        print('____________________________________________')










