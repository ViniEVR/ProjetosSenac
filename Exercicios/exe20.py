import menu

def mediaCidadao():
    try:
        print('A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes.' +
              'Faça um algoritmos para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:\n' +
            'a) Média de salário da população\n'  + 'b) Média do número de filhos\n' + 'c) Maior salário dos habitantes\n' + 'd) Percentual de pessoas com salário menor que R$ 150,00 \n')

        salario = []
        filho = []
        salarioMin = 0
        s = 1

        while not s < 0:
            s = float(input('Digite o salário: '))
            if s < 0:
                print('Salário negativo digitado, obrigado por utilizar o programa :), aqui estão as suas estatísticas: ')
                print('A média do salário: ' + str(sum(salario) / len(salario)) +
                      '\nA média do número de filhos: ' + str(sum(filho) / len(filho)) +
                      '\nO maior salário: ' + str(max(salario)) +
                      '\nPercentual de pessoas com salário menor do que R$150,00: ' + str((salarioMin / len(salario)) * 100))

                print(menu.retornarMenu())

            f = int(input('Digite a quantidade de filhos: '))

            while f < 0:
                print('\n\n______________________________________________________________')
                print('\nDigite uma quantidade de filhos válida\n')
                print('______________________________________________________________\n\n')
                f = int(input('Digite a quantidade de filhos: '))

            else:
                if s < 150:
                    salarioMin += 1
                salario.append(s)
                filho.append(f)
    except:
        print('\n\n______________________________________________________________')
        print('\nDigite números válidos\n')
        print('______________________________________________________________\n\n')
        mediaCidadao()




