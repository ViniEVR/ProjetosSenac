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
    print('Escolha um dos exercicios abaixo: \n ' +
          '\n.Exercicio - 1' +
          '\n.Exercicio - 2' +
          '\n.Exercicio - 3' +
          '\n.Exercicio - 4' +
          '\n.Exercicio - 5')

    this.opcao = int(input()) #Coletar