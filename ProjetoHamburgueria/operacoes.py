import mysql.connector
import conexao
import conta
import funcionario
import lanches
import cardapio
import sobremesas
import bebidas

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserirLanches(nome, ingredientes, preco):
    try:
        sql = f"INSERT INTO lanche(codigo, nome, ingredientes, preco) values('','{nome}','{ingredientes}','{preco}')"
        con.execute(sql) #Prepara o comando para ser executado
        db_connection.commit() #Executa o comando no banco de dados
        print(con.rowcount, "")
    except Exception as erro:
        print(erro)
        print('____________________________________________')
        print('\nDigite um valor válido\n')
        print('____________________________________________')
        funcionario.menu()

def inserirBebidas():
    try:
        sql = f"INSERT INTO bebida(codigo, nome, preco) values('','{nome}','{preco}')"
        con.execute(sql)  # Prepara o comando para ser executado
        db_connection.commit()  # Executa o comando no banco de dados
        print(con.rowcount, "")
    except Exception as erro:
        print(erro)

def inserirSobremesas():
    try:
        sql = "sobremesas() values('','{}','{}','{}','{}')".format()
        con.execute(sql) #Prepara o comando para ser executado
        db_connection.commit() #Executa o comando no banco de dados
        print(con.rowcount, "")
    except Exception as erro:
        print(erro)

#Consultar os dados do DB
def selecionarLanche():
    try:
        sql = "select * from lanche"
        con.execute(sql)
        print('\n')

        for(codigo, nome, ingredientes, preco) in con:
            print(codigo, nome, ingredientes, preco)
            print('\n')
    except Exception as erro:
        print(erro)

def contaLanche(codigo):
    try:
        if codigo == -1:
            cardapio.redirecionarCardapio()
        sql = f"select nome, preco from lanche where codigo = '{codigo}'"
        con.execute(sql)

        for (nome, preco) in con:
            print(nome, preco)

        print('____________________________________________')
        print(f'\nVocê adicionou {nome} ao seu pedido\n')
        print('____________________________________________')

        conta.calculoValor(preco, nome)

    except Exception as erro:
        print('____________________________________________')
        print('\nDigite uma opção válida\n')
        print('____________________________________________')
        lanches.selecionarLanches()


#Consultar os dados do DB
def selecionarBebida():
    try:
        sql = "select * from bebida"
        con.execute(sql)

        for(codigo, nome, preco) in con:
            print(codigo, nome, preco)
            print('\n')
    except Exception as erro:
        print(erro)

#Consultar os dados do DB
def selecionarSobremesa():
    try:
        sql = "select * from sobremesa"
        con.execute(sql)

        for(codigo, nome, ingredientes, preco) in con:
            print(codigo, nome, ingredientes, preco)
            print('\n')
    except Exception as erro:
        print(erro)



def contaBebida(codigo):
    try:
        if codigo == -1:
            cardapio.redirecionarCardapio()
        sql = f"select nome, preco from bebida where codigo = '{codigo}'"
        con.execute(sql)

        for (nome, preco) in con:
            print(nome, preco)

        print('____________________________________________')
        print(f'\nVocê adicionou {nome} ao seu pedido\n')
        print('____________________________________________')

        conta.calculoValor(preco, nome)

    except Exception as erro:
        print('____________________________________________')
        print('\nDigite uma opção válida\n')
        print('____________________________________________')
        bebidas.selecionarBebidas()

def contaSobremesa(codigo):
    try:
        if codigo == -1:
            cardapio.redirecionarCardapio()
        sql = f"select nome, preco from sobremesa where codigo = '{codigo}'"
        con.execute(sql)

        for (nome, preco) in con:
            print(nome, preco)

        print('____________________________________________')
        print(f'\nVocê adicionou {nome} ao seu pedido\n')
        print('____________________________________________')

        conta.calculoValor(preco, nome)

    except Exception as erro:
        print('____________________________________________')
        print('\nDigite uma opção válida\n')
        print('____________________________________________')
        sobremesas.selecionarSobremesas()

