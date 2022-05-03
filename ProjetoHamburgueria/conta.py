import this

#Classe responsável por calcular o valor da conta
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

def contaComItens():

    j = 0
    for i in item:
        print(f"\n\n{i}, valor: R${precoTotal[j]}0")
        j += 1

    print('____________________________________________')
    print('\nValor da sua conta é de \nR$:' + this.valorConta)
    print('____________________________________________')






