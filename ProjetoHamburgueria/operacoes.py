import mysql.connector
import conexao
import conta
import funcionario
import lanches
import cardapio
import sobremesas
import bebidas
import this

this.codigoLanche = ""


db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserirLanches(nome, ingredientes, preco):
    try:
        if preco <= 0 or nome == "" or ingredientes == "":

            while nome == "" or nome == " ":
                nome = input('Digite o nome do lanche: ')
                ingredientes = input('\nDigite os ingredientes: ')
                preco = int(input('\nDigite o valor: R$'))

            return "Digite valores válidos"
        else:
            sql = f"INSERT INTO lanche(codigo, nome, ingredientes, preco) values('','{nome}','{ingredientes}','{preco}')"
            con.execute(sql) #Prepara o comando para ser executado
            db_connection.commit() #Executa o comando no banco de dados
            print("Lanche cadastrado com sucesso!")
    except Exception as erro:
        return erro
        funcionario.menu()

def excluirLanche(codigo):
    try:
        sql = f"DELETE FROM lanche WHERE codigo = {codigo}"
        con.execute(sql) #Prepara o comando para ser executado
        db_connection.commit() #Executa o comando no banco de dados
        print("Lanche deletado com sucesso!")
    except Exception as erro:
        print(erro)
        print('____________________________________________')
        print('\nDigite valores válidos\n')
        print('____________________________________________')
        funcionario.menu()

def inserirBebidas(nome, preco):
    try:
        if preco <= 0 or nome == "":
            print('____________________________________________')
            print('\nDigite valores válidos\n')
            print('____________________________________________')
            funcionario.mostrarMenu()
        else:
            sql = f"INSERT INTO bebida(codigo, nome, preco) VALUES('','{nome}','{preco}')"
            con.execute(sql)  # Prepara o comando para ser executado
            db_connection.commit()  # Executa o comando no banco de dados
            print("Bebida cadastrada com sucesso!")
    except Exception as erro:
        print(erro)

def excluirBebida(codigo):
    try:
        sql = f"DELETE FROM bebida WHERE codigo = {codigo}"
        con.execute(sql) #Prepara o comando para ser executado
        db_connection.commit() #Executa o comando no banco de dados
        print("Bebida deletada com sucesso!")
    except Exception as erro:
        print(erro)
        print('____________________________________________')
        print('\nDigite valores válidos\n')
        print('____________________________________________')
        funcionario.menu()



def inserirSobremesas(nome, ingredientes, preco):
    try:
        if preco <= 0 or nome == "" or ingredientes == "":
            print('____________________________________________')
            print('\nDigite valores válidos\n')
            print('____________________________________________')
            funcionario.mostrarMenu()
        else:
            sql = f"INSERT INTO sobremesa(codigo, nome, ingredientes, preco) values('','{nome}','{ingredientes}','{preco}')"
            con.execute(sql)  # Prepara o comando para ser executado
            db_connection.commit()  # Executa o comando no banco de dados
            print("Sombremesa cadastrada com sucesso!")
    except Exception as erro:
        print(erro)
        print('____________________________________________')
        print('\nDigite valores válidos\n')
        print('____________________________________________')
        funcionario.menu()

def excluirSobremesa(codigo):
    try:
        sql = f"DELETE FROM sobremesa WHERE codigo = {codigo}"
        con.execute(sql) #Prepara o comando para ser executado
        db_connection.commit() #Executa o comando no banco de dados
        print("Sobremesa deletada com sucesso!")
    except Exception as erro:
        print(erro)
        print('____________________________________________')
        print('\nDigite um valor válido\n')
        print('____________________________________________')
        funcionario.menu()



#Consultar os dados do DB
def selecionarCodigoLanche():
    vetorCodigo = []
    try:
        sql = "select codigo from lanche"
        con.execute(sql)

        
        for(codigo) in con:
            this.msg = str(codigo).replace("(","")
            this.msg = this.msg.replace(")", "")
            this.msg = this.msg.replace(",","")
            vetorCodigo.append(this.msg)

        return vetorCodigo
               
    except Exception as erro:
        return (erro)

def selecionarNomeLanche():
    try:
        vetorNome = []
        this.msg = ""
        sql = "select nome from lanche"
        con.execute(sql)
        
        for(nome) in con:
            this.msg = str(nome).replace("(","")
            this.msg = this.msg.replace(")", "")
            this.msg = this.msg.replace(",","")
            this.msg = this.msg.replace("'","")
            vetorNome.append(this.msg)
            

        return vetorNome
               
    except Exception as erro:
        return (erro)

def selecionarIngredienteLanche():
    try:
        vetorIngrediente = []
        this.msg = ""
        sql = "select ingredientes from lanche"
        con.execute(sql)
        
        for(nome) in con:
            this.msg = str(nome).replace("(","")
            this.msg = this.msg.replace(")", "")
            this.msg = this.msg.replace("'","")

            vetorIngrediente.append(this.msg)
            

        return vetorIngrediente
               
    except Exception as erro:
        return (erro)

def selecionarValorLanche():
    try:
        vetorPreco = []
        this.msg = ""
        sql = "select preco from lanche"
        con.execute(sql)

        this.precoLanche = ""

        
        for(preco) in con:

            this.msg = 'R$ ' + str(preco).replace("(","") + '0'
            this.msg = this.msg.replace(")", "")
            this.msg = this.msg.replace(",","")
            this.msg = this.msg.replace("'","")
            

            vetorPreco.append(this.msg)
            

        return vetorPreco
               
    except Exception as erro:
        return (erro)

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

def inserirFuncionario(nome, senha):
    try:
        if nome == "" or senha == "":
            print('____________________________________________')
            print('\nDigite um nome e uma senha válidos\n')
            print('____________________________________________')
        else:
            sql = "insert into funcionario(codigo, nome, senha) values('','{}','{}')".format(nome, senha)
            con.execute(sql) #Prepara o comando para ser executado
            db_connection.commit() #Executa o comando no banco de dados
            print(con.rowcount, "Inserido!")
    except Exception as erro:
        print(erro)

def excluirFuncionario(codigo):
    try:
        sql = f"DELETE FROM funcionario WHERE codigo = {codigo}"
        con.execute(sql) #Prepara o comando para ser executado
        db_connection.commit() #Executa o comando no banco de dados
        print("Funcionario deletado com sucesso!")
    except Exception as erro:
        print(erro)
        print('____________________________________________')
        print('\nDigite um valor válido\n')
        print('____________________________________________')
        funcionario.menu()        

def atualizar(codigo, campo, novoDado):
    try:
        sql = "update lanche set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro


def atualizarBebida(codigo, campo, novoDado):
    try:
        sql = "update Bebida set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro        

def atualizarSobremesa(codigo, campo, novoDado):
    try:
        sql = "update sobremesa set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro      

def atualizarFuncionario(codigo, campo, novoDado):
    try:
        sql = "update funcionario set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro                 

