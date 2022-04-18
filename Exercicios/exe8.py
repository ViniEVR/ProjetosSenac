
nota1 = 0
nota2 = 0
nota3 = 0
mediaFinal = 0


def notaErrada():
    print('\n\n______________________________________________________________')
    print('\nDigite uma nota de 0 a 10\n')
    print('______________________________________________________________\n\n')
    media()

def media():
    try:
        print('Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno')

        print('Informe a primeira nota: ')
        nota1 = float(input())

        if nota1 < 0 or nota1 > 10:
            notaErrada()
        else:
            print('Informe a segunda nota: ')
            nota2 = float(input())
            if nota2 < 0 or nota2 > 10:
                notaErrada()
            else:
                print('Informe a terceira nota: ')
                nota3 = float(input())
                if nota3 < 0 or nota3 > 10:
                        notaErrada()
                else:
                    mediaFinal = str((nota1 + nota2 + nota3) / 3)

                    print('A media do aluno é ' + mediaFinal)
    except:
        notaErrada()