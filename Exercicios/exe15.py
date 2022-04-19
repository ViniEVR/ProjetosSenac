import this

this.negativo = 0
this.negativo1 = 0
this.lista1 = []

def negativos():
    try:

        print('Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.')

        lista = []
        for i in range(10):
            x = int(input("Digite o " + str(i + 1) + 'º valor: '))
            while x in lista:
                print('Valor já presente na lista, adicione outro valor')
                x = int(input("Digite o " + str(i + 1) + 'º valor: '))
            else:
                lista.append(x)
                if x < 0:
                    this.negativo += 1
                    this.lista1.append(x)


        lista.sort()
        this.lista1.sort()
        this.lista1.reverse()
        print('Os números digitados foram ' + str(lista) + '\n' + 'Dentre eles estão ' + str(this.negativo) + ' negativos \n' +
        'Sendo eles: ' + str(this.lista1))
    except:
        print('\n\n______________________________________________________________')
        print('\nDigite um número válido\n')
        print('______________________________________________________________\n\n')
        negativos()