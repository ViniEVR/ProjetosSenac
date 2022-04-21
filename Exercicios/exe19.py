
def mediaAlunos():
    try:
        print('Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. ' +
              'Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada.' +
                'Escrever a média da turma e o resultado da contagem.')

        lista = []
        acimaDaMedia = 0
        media = 0
        maior = 0
        for i in range(5):
            x = int(input("Digite da nota do " + str(i + 1) + 'º aluno: '))
            while x < 0 or x > 10:
                print('\n\n______________________________________________________________')
                print('\nDigite uma nota superior ou igual a 0 e inferior ou igual a 10\n')
                print('______________________________________________________________\n\n')
                x = int(input("Digite da nota do " + str(i + 1) + 'º aluno: '))
            else:
                lista.append(x)
                #Caso queria ver as notas sendo adicionas na lista -> print(lista)

        print('teste')
        media = sum(lista) / len(lista)
        maior = max(lista)

        for i in lista:
            if i > media:
                acimaDaMedia += 1
        print('A média dos alunos foi de ' + str(media) + '\nA maior nota foi de: ' + str(maior) +
                '\nE a quantidade de notas acima da média foi de ' + str(acimaDaMedia))
    except:
        print('\n\n______________________________________________________________')
        print('\nHouve um problema\n')
        print('______________________________________________________________\n\n')
        mediaAlunos()





