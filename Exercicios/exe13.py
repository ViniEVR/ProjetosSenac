
num = 0
num1 = 0

def tabuada():
    try:
        print('Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.')

        num = int(input('Digite um número inteiro:'))
        while num < 1:
            print('\n\n______________________________________________________________')
            print('\nDigite um número positivo\n')
            print('______________________________________________________________\n\n')
            num = int(input('Digite um número inteiro:'))

        for i in range(10):
            num1 = str(num * (i + 1))

            print('{} X {} = '.format(num, i + 1) + num1)
    except:
        print('\n\n______________________________________________________________')
        print('\nDigite um número válido\n')
        print('______________________________________________________________\n\n')
        tabuada()

