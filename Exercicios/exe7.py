custoFabrica = 0
totalCarro = 0
impostos = 0
distribuidor = 0

def valorCarro():
   try:
        print('O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).\n' +
              'Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de\n' +
                'fábrica de um carro, calcular e escrever o custo final ao consumidor')

        print('Informe o custo de fábrica:')
        custoFabrica = float(input())

        if custoFabrica < 0:
            print('\n\n_________________________________________________________________________')
            print('\nO custo de fábrica não pode ser negativo\n')
            print('_________________________________________________________________________\n\n')
            valorCarro()
        else:
            impostos = (custoFabrica * 45 / 100)
            distribuidor = (custoFabrica * 28 / 100)
            totalCarro = str(custoFabrica + impostos + distribuidor)

            print('O valor total do carro é de R$' + totalCarro)

   except:
       print('\n\n______________________________________________________________')
       print('\nDigite apenas números positivos\n')
       print('______________________________________________________________\n\n')
       valorCarro()
