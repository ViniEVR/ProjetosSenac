
numeroConta = 0
valorSaldo = 0
valorDebito = 0
valorCredito = 0
saldoAtual = 0
def saldo():
    try:
        print('Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e \n' +
        'escrever o saldo atual (saldo atual = saldo - débito + crédito).\n' +
        'Também testar se saldo atual for maior ou igual a zero escrever a mensagem SaldoPositivo, senão escrever a mensagem Saldo Negativo.')

        numeroConta = int(input('Informe o número da conta: '))

        while numeroConta < 0:
            print('Informe um número de conta válido e positivo\n')
            numeroConta = int(input('Informe o número da conta: '))


        valorSaldo = float(input('Informe o saldo:'))

        while valorSaldo < 0:
            print('\n\n______________________________________________________________')
            print('\nDigite um valor válido\n')
            print('______________________________________________________________\n\n')

        valorDebito = float(input('Informe o valor do débito:'))
        while valorDebito < 0:
            print('Informe um valor positivo')
            valorDebito = float(input('Informe o valor do débito:'))


        valorCredito = float(input('Informe o valor do crédito:'))
        while valorCredito < 0:
            print('Informe um valor positivo')
            valorCredito = float(input('Informe o valor do crédito:'))

        saldoAtual = (valorSaldo - valorDebito + valorCredito)

        if saldoAtual < 0:
            print('\n\n______________________________________________________________')
            print('\nSaldo negativo\n')
            print('______________________________________________________________\n\n')
            print('Seu saldo é: R$' + str(saldoAtual))
        else:
            print('\n\n______________________________________________________________')
            print('\nSaldo positivo\n')
            print('______________________________________________________________\n\n')
            print('Seu saldo é: R$' + str(saldoAtual))

    except:
        print('\n\n______________________________________________________________')
        print('\nDigite um número válido\n')
        print('______________________________________________________________\n\n')
        saldo()









