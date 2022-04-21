import this

this.negativo = 0
this.negativo1 = 0
this.soma = 0
this.lista1 = []


def somaValores():
    try:
        print('Escreva um algoritmo para ler 10 números.' +
              'Todos os números lidos com valor inferior a 40 devem ser somados.' +
              'Escreva o valor final da soma efetuada.')

        lista = []
        for i in range(10):
            x = int(input("Digite o " + str(i + 1) + 'º valor: '))
            while x in lista:
                print('Valor já presente na lista, adicione outro valor')
                x = int(input("Digite o " + str(i + 1) + 'º valor: '))
            else:
                lista.append(x)
                if x < 40:
                    this.soma += x
                    this.lista1.append(x)

        lista.sort()
        this.lista1.sort()
        print(lista)
        print('A soma dos valores digitados inferiores a 40 é: ' + str(this.soma))
    except:
        print('\n\n______________________________________________________________')
        print('\nDigite valores válidos\n')
        print('______________________________________________________________\n\n')
        somaValores()