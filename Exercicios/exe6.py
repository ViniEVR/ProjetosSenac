salario = 0
reajuste = 0
percentual = 0

def reajusteSalario():
    try:
        print('Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.\n' +
              'Calcular e escrever o valor do novo salário.')



        print('Informe o salário:')
        salario = float(input())



        if salario < 0:
            print('\n\n______________________________________________________________')
            print('\nDigite um salário válido\n')
            print('______________________________________________________________\n\n')
            reajusteSalario()
        else:
            print('Digite o percentual de reajuste:')
            reajuste = float(input())


            if reajuste < 0:
                print('\n\n______________________________________________________________')
                print('\nInforme um valor de reajuste positivo\n')
                print('______________________________________________________________\n\n')
                reajusteSalario()
            else:
                percentual = str(salario + (salario * reajuste ) / 100)
                print('\nO valor do novo salário será de R$' + percentual + '\n' )

    except:
        print('\n\n______________________________________________________________')
        print('\nDigite apenas números positivos\n')
        print('______________________________________________________________\n\n')
        reajusteSalario()


