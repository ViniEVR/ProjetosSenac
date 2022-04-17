import this

this.num1 = 0

def antecessor():
    try:
        print('Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor.')
        print("\nDigite um valor:")
        this.num1 = int(input())

        num2 = this.num1 - 1
        print("\nO valor antecessor de {} é {}".format(this.num1, num2))
    except:
        print('\n\n______________________________________________________________')
        print('\nDigite valores inteiros ou reais, sem letras ou simbolos\n')
        print('______________________________________________________________\n\n')
        antecessor()