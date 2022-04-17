import this

this.a = 10
this.b = 20
this.c = 0

def trocarValores():
    print('Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.\n' +
          'A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa.\n' +
          'Ao final, escrever os valores que ficaram armazenados nas variáveis')

    print('\nO valor da váriavel A antes da troca é A = {} e o valor da variável B antes da troca é de B = {}\n'.format(this.a, this.b))

    this.c = this.a
    this.a = this.b
    this.b = this.c

    print('E após a troca o valor de A = {} e o valor de B = {}'.format(this.a, this.b))

