import mysql.connector
import conexao

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserirLanches():
    try:
        sql = "lanches() values('','{}','{}','{}','{}')".format()
        con.execute(sql) #Prepara o comando para ser executado
        db_connection.commit() #Executa o comando no banco de dados
        print(con.rowcount, "")
    except Exception as erro:
        print(erro)

def inserirBebidas():
    try:
        sql = "bebidas() values('','{}','{}','{}','{}')".format()
        con.execute(sql) #Prepara o comando para ser executado
        db_connection.commit() #Executa o comando no banco de dados
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

        for(codigo, nome, ingredientes, preco) in con:
            print(codigo, nome, ingredientes, preco)
            print('\n')
    except Exception as erro:
        print(erro)

#Consultar os dados do DB
def selecionarBebida():
    try:
        sql = "select * from bebida"
        con.execute(sql)

        for(codigo, nome, ingredientes, preco) in con:
            print(codigo, nome, ingredientes, preco)
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
