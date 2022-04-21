import this
import menu

nums = [15, 100]
this.soma = 0
this.quantidade = 0
def mediaAritmetica():
    try:
        print('Faça um algoritmo que calcule e escreva a média aritmética dos números inteiros entre 15 (inclusive) e 100 (inclusive)')
        #print('A média aritmética dos números entre 15 e 100 incluindo os mesmos é de: ' + str(sum(nums) / len(nums))) <- Jeito simples

        for i in range(15, 101):
            this.soma += i
            this.quantidade += 1

            media = this.soma / this.quantidade

        print('A média aritmética dos números entre 15 e 100 incluindo os mesmos é de: ' + str(media))
    except:
        print('\n\n______________________________________________________________')
        print('\nUm erro aconteceu\n')
        print('______________________________________________________________\n\n')
        menu.retornarMenu()

