
salarioFixo = 0
valorVendido = 0
valorVendido1 = 0
salarioTotal = 0
def vendas():
    try:
        print('Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.\n' +
              'Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% ' +
              'sobre o que ultrapassar este valor, calcular e escrever o seu salário total.')

        salarioFixo = float(input('Informe o salário fixo: '))
        while salarioFixo < 0:
            print('\n\n______________________________________________________________')
            print('\nDigite um salário positivo\n')
            print('______________________________________________________________\n\n')
            salarioFixo = float(input('Informe o salário fixo: '))

        valorVendido = float(input('Informe a soma das vendas de valor inferior a R$1500: R$'))
        while valorVendido < 0:
            print('\n\n______________________________________________________________')
            print('\nDigite um valor positivo\n')
            print('______________________________________________________________\n\n')
            valorVendido = float(input('Informe a soma das vendas de valor inferior a R$1500: R$'))

        valorVendido1 = float(input('Informe a soma das vendas de valor superior a R$1500: R$'))
        while valorVendido1 < 0:
            print('\n\n______________________________________________________________')
            print('\nDigite um valor positivo\n')
            print('______________________________________________________________\n\n')
            valorVendido1 = float(input('Informe a soma das vendas de valor superior a R$1500: R$'))

        salarioTotal = str((valorVendido * 0.03) + (valorVendido1 * 0.05) + salarioFixo)

        print('O salário total é de R$' + salarioTotal)

    except:
        print('\n\n______________________________________________________________')
        print('\nDigite um valor válido\n')
        print('______________________________________________________________\n\n')
        vendas()

