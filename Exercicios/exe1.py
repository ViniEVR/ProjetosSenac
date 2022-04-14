import this

this.a = 10
this.b = 20
this.c = 0

def trocarValores():
    print('\nO valor da váriavel A antes da troca é A = {} e o valor da variável B antes da troca é de B = {}\n'.format(this.a, this.b))

    this.c = this.a
    this.a = this.b
    this.b = this.c

    print('E após a troca o valor de A = {} e o valor de B = {}'.format(this.a, this.b))
