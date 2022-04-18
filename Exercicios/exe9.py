

quantidadeMacas = 0
precoMacas = 0

def macas():
    try:
        print('As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12.\n' +
              'Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total dacompra.')

        print('Quantas maçãs você deseja?')
        quantidadeMacas = int(input())

        if quantidadeMacas < 0:
            print('\n\n______________________________________________________________')
            print('\nInforme um valor igual ou superior a 1\n')
            print('______________________________________________________________\n\n')
            macas()
        else:
            if quantidadeMacas < 12:
                precoMacas = str(quantidadeMacas * 1.30)
            else:
                precoMacas = str(quantidadeMacas * 1)

        print('O valor total a ser pago é de R$' + precoMacas)


    except:
        print('\n\n______________________________________________________________')
        print('\nDigite um valor válido\n')
        print('______________________________________________________________\n\n')
        macas()