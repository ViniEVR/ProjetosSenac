
def numerosLidos():
    try:
        print(' Faça um algoritmo para ler uma quantidade e a seguir ler esta quantidade de números.'+
        'Depois de ler todos os números o algoritmo deve apresentar na tela o maior dos números lidos e a média dos números lidos.')

        lista = []
        j = int(input('Quantos números você deseja digitar?: '))
        for i in range(j):
            x = int(input("Digite o " + str(i + 1) + 'º valor: '))
            lista.append(x)

        print('Os números digitados foram: ' + str(lista) + '\nO maior dentre esses números é: ' + str(max(lista)) +
              '\nA média dos valores presentes na lista é de: ' + str(sum(lista) / len(lista)))

    except:
        print('\n\n______________________________________________________________')
        print('\nDigite valores válidos\n')
        print('______________________________________________________________\n\n')
        numerosLidos()


