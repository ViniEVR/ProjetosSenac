import this

this.totalEleitores = 0
this.votosBrancos = 0
this.votosNulos = 0
this.votosValidos = 0

try:
    def total():
        print('Informe o total de eleitores:')
        this.totalEleitores = int(input())

        if this.totalEleitores < 1:
            print('\n\n______________________________________________________________')
            print('\nInforme uma quantidade válida de eleitores\n')
            print('______________________________________________________________\n\n')
            total()
        else:
            branco()


    def branco():
        print('Informe o total de votos brancos:')
        this.votosBrancos = int(input())

        if this.votosBrancos < 0 or this.votosBrancos > this.totalEleitores:
            print('\n\n_________________________________________________________________________')
            print('\nO valor não pode ser negativo e nem superior ao valor total de eleitores\n')
            print('_________________________________________________________________________\n\n')
            total()
        else:
            nulo()

    def nulo():
        print('Informe o total de votos nulos:')
        this.votosNulos = int(input())

        if this.votosNulos < 0 or (this.votosNulos + this.votosBrancos) > this.totalEleitores:
            print('\n\n_________________________________________________________________________')
            print('\nO valor não pode ser negativo e nem superior ao valor total de eleitores\n')
            print('_________________________________________________________________________\n\n')
            total()
        else:
            valido()

    def valido():
        print('Informe o total de votos válidos')
        this.votosValidos = int(input())

        if this.votosValidos < 0 or (this.votosValidos + this.votosNulos + this.votosBrancos) > this.totalEleitores:
            print('\n\n_________________________________________________________________________')
            print('\nO valor não pode ser negativo e nem superior ao valor total de eleitores\n')
            print('_________________________________________________________________________\n\n')
            total()
        else:
            porcentagem()

    def porcentagem():
        porcentagemBrancos = str((this.votosBrancos / this.totalEleitores) * 100)

        porcentagemNulos = str((this.votosNulos / this.totalEleitores) * 100)

        porcentagemValidos = str((this.votosValidos / this.totalEleitores) * 100)

        print('O número total de eleitores é: ' + str(this.totalEleitores) +
              '\n\nO percentual de votos brancos é de: ' + porcentagemBrancos + '%' +
              '\n\nO percentual de votos nulos é de: ' + porcentagemNulos + '%' +
              '\n\nO percentual de votos válidos é de: ' + porcentagemValidos + '%')

except:
    print('\n\n______________________________________________________________')
    print('\nDigite apenas valores inteiros\n')
    print('______________________________________________________________\n\n')
    total()
