import this

this.base = 0
this.altura = 0

def areaRetangulo():
    try:
        print("Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo. (Base X Altura).")

        print('\nDigite o valor da base do retângulo:')
        this.base = float(input())

        print('\nDigite o valor da altura do retângulo:')
        this.altura = float(input())

        area = str(this.base * this.altura)

        print('A área do retângulo é de ' + area)
    except:
        print('\n\n______________________________________________________________')
        print('\nDigite valores inteiros ou reais, sem letras ou simbolos\n')
        print('______________________________________________________________\n\n')
        areaRetangulo()