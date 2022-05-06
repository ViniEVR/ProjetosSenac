import operacoes
import  this

this.opcao = -1

def menu():
    print("Escolha uma das opções abaixo: \n\n" +
          "1.Cadastrar\n" +
          "2.Consultar\n" +
          "3.Atualizar\n" +
          "4.Atualizar telefone\n" +
          "5.Atualizar endereço\n" +
          "6.Atualizar data atual\n" +
          "7.Excluir\n" +
          "0.Sair")
    this.opcao = int(input('\nOpção selecionada:'))

def operacao():
    try:
        while (this.opcao != 0):
            menu()
            if this.opcao == 1:
                nome = input('Digite o nome: ')
                telefone = input('\nDigite o telefone: ')
                endereco = input('\nDigite o endereço: ')
                dataAtual = input('\nDigite a data atual: ')

                # Utilizar o método cadastrar
                operacoes.inserir(nome, telefone, endereco, dataAtual)

            elif this.opcao == 2:
                operacoes.selecionar()

            elif this.opcao == 3:
                codigo = int(input('Informe o código: '))
                nome = input('Informe o novo nome: ')

                # Uso do método
                operacoes.atualizarNome(codigo, nome)

            elif this.opcao == 4:
                codigo = int(input('Informe o código: '))
                telefone = input('Informe o novo telefone: ')

                # Uso do método
                operacoes.atualizarTelefone(codigo, telefone)

            elif this.opcao == 5:
                codigo = int(input('Informe o código: '))
                endereco = input('Informe o novo endereço: ')

                # Uso do método
                operacoes.atualizarEndereco(codigo, endereco)

            elif this.opcao == 6:
                codigo = int(input('Informe o código: '))
                dataAtual = input('Informe a nova data atual: ')

                # Uso do método
                operacoes.atualizarTelefone(codigo, dataAtual)

            elif this.opcao == 7:
                codigo = int(input('Informe o código: '))
                operacoes.excluir()

            elif this.opcao == 0:
                print('Obrigado!')
    except:
        print('Erro, digite informações válidas')
        operacao()




