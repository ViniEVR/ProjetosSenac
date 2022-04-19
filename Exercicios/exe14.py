
n = 0

def inteiros():
    try:
        print('Ler um valor N e imprimir todos os valoresinteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO.')

        n = int(input('Informe um valor inteiro:'))
        while n < 1:
            print('\n\n______________________________________________________________')
            print('\nDigite um número positivo ou maior do que 0\n')
            print('______________________________________________________________\n\n')
            n = int(input('Informe um valor inteiro:'))


        for i in range(n):
            print(i + 1)

    except:
        print('\n\n______________________________________________________________')
        print('\nDigite um número válido\n')
        print('______________________________________________________________\n\n')
        inteiros()