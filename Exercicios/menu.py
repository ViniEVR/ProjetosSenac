import this

this.opcao = 0 #Global
var1 = 0
var2 = 0

def coletarVar1():
    print('Informe o primeiro número: ')
    this.var1 = float(input())

def coletarVar2():
    print('Informe o segundo número: ')
    this.var2 = float(input())

def mostrarMenu():
    print('Escolha um dos exercicios abaixo: \n ')
    print('Sair - ' + str(0))
    for i in range(1, 20 + 1):
        i + 1
        print('Exercicio - ' + str(i))

    this.opcao = int(input()) #Coletar

def lista():
    #Mostrar o menu em tela
    while this.opcao != 0:
        mostrarMenu()
