

def valores():
    try:
        print('Ler 10 valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente')
        lista = []
        for i in range(10):
            x = int(input("Digite o " + str(i + 1) + 'º valor: '))
            while x in lista:
                print('Valor já presente na lista, adicione outro valor')
                x = int(input("Digite o " + str(i + 1) + 'º valor: '))
                lista.append(x)
            else:
                lista.append(x)

        lista.sort()
        print(lista)

    except:
        print('\n\n______________________________________________________________')
        print('\nDigite um numero inteiro\n')
        print('______________________________________________________________\n\n')