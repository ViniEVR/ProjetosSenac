import this

this.anos = 0
this.meses = 0
this. dias = 0

def idade():
    try:
        print('Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias.' +
              'Considerar ano com 365 dias e mês com 30 dias.')

        print('\nQuantos anos você tem?')
        this.anos = int(input())

        print('\nOkay, ' + str(this.anos) + ' anos e quantos meses?')
        this.meses = int(input())

        print('\nCerto, ' + str(this. anos) + ' anos, ' + str(this.meses) + ' meses e quantos dias mesmo?')
        this.dias = int(input())

        print('\nParabéns!, você viveu durante ' + str(this.anos * 365 + this.meses * 30 + this.dias) + ' dias e eu espero que você viva por muito mais, ainda chegaremos aos 200 anos :)')
    except:
        print('\n\n______________________________________________________________')
        print('\nDigite apenas valores inteiros\n')
        print('______________________________________________________________\n\n')
        idade()
