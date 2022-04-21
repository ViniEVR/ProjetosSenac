import this
import exe1
import exe2
import exe3
import exe4
import exe5
import exe6
import exe7
import exe8
import exe9
import exe10
import exe11
import exe12
import exe13
import exe14
import exe15
import  exe16
import exe17
import exe18
import exe19
import exe20

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
    try:
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
            elif this.opcao == 6:
                print(exe6.reajusteSalario())

                print(retornarMenu())
            elif this.opcao == 7:
                print(exe7.valorCarro())

                print(retornarMenu())
            elif this.opcao == 8:
                print(exe8.media())

                print(retornarMenu())
            elif this.opcao == 9:
                print(exe9.macas())

                print(retornarMenu())
            elif this.opcao == 10:
                print(exe10.valores())

                print(retornarMenu())
            elif this.opcao == 11:
                print(exe11.vendas())

                print(retornarMenu())
            elif this.opcao == 12:
                print(exe12.saldo())

                print(retornarMenu())
            elif this.opcao == 13:
                print(exe13.tabuada())

                print(retornarMenu())
            elif this.opcao == 14:
                print(exe14.inteiros())

                print(retornarMenu())
            elif this.opcao == 15:
                print(exe15.negativos())

                print(retornarMenu())
            elif this.opcao == 16:
                print(exe16.somaValores())

                print(retornarMenu())
            elif this.opcao == 17:
                print(exe17.mediaAritmetica())

                print(retornarMenu())
            elif this.opcao == 18:
                print(exe18.numerosLidos())

                print(retornarMenu())
            elif this.opcao == 19:
                print(exe19.mediaAlunos())

                print(retornarMenu())
            elif this.opcao == 20:
                print(exe20.mediaCidadao())

                print(retornarMenu())
            else:
                print('Opção escolhida inválida, favor escolher uma das opções listadas\n' +
                      'Pressione enter para tentar novamente: ')
                input()
                mostrarMenu()
    except:
        print('\n\n______________________________________________________________')
        print('\nEscolha uma das opções disponiveis\n')
        print('______________________________________________________________\n\n')
        lista()


