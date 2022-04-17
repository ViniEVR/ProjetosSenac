import this
import exe1
import exe2
import exe3
import exe4
import exe5

this.opcao = -1 #Global

def mostrarMenu():
    print('Escolha um dos exercicios abaixo: \n ')
    print('Sair - ' + str(0))
    for i in range(1, 20 + 1):
        i + 1
        print('Exercicio - ' + str(i))

    this.opcao = int(input()) #Coletar

def retornarMenu():
    #Método para dar opção de retornar ao menu entre um exercicio e outro
    opcao1 = 0
    print('\n\nDeseja retornar ao menu?\n' +
          '1.Sim\n' +
          '2.Não, sair do programa')
    opcao1 = int(input())
    if opcao1 == 1:
        lista()
    elif opcao1 == 2:
        print('Obrigado por utilizar o programa :)')
        this.opcao = 0 #Quebrando o loop passando o valor 0 no while da lista()
    else:
        print('\n\nDigite uma opção válida e tente novamente')
        retornarMenu()



def lista():
    #Mostrar o menu em tela
    while this.opcao != 0:
        mostrarMenu()
        if this.opcao == 0:
            #Finalizando o programa
            print('Obrigado por utilizar o programa :)')

        elif this.opcao == 1:
            print(exe1.trocarValores())

            print(retornarMenu())

        elif this.opcao == 2:
            print(exe2.antecessor())

            print(retornarMenu())
        elif this.opcao == 3:
            print(exe3.areaRetangulo())

            print(retornarMenu())
        elif this.opcao == 4:
            print(exe4.idade())

            print(retornarMenu())
        elif this.opcao == 5:
            print(exe5.total())

            print(retornarMenu())
        else:
            print('Opção escolhida inválida, favor escolher uma das opções listadas\n' +
                  'Pressione enter para tentar novamente: ')
            input()
            mostrarMenu()


