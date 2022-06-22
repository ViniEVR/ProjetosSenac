import conexaoBD
import mysql.connector
import this
this.msg = ""
db_connection = conexaoBD.conexao()
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = f"Insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('', '{nome}', '{telefone}', '{endereco}', '{dataDeNascimento}')"
        con.execute(sql)
        db_connection.commit()
        return con.rowcount,"Inserido!"
    except Exception as erro:
        return erro

def consultar():
    try:
        sql = "select * from pessoa"
        con.execute(sql)

        this.msg = ""
        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            this.msg += f"Código: {codigo}, Nome: {nome}, Telefone: {telefone}, Endereco: {endereco}, Data de nascimento: {dataDeNascimento}"

        return this.msg

    except Exception as erro:
        return erro

def consultarTudo(cod):
    try:
        sql = f"select * from pessoa where codigo = '{cod}'"
        con.execute(sql)

        this.msg = ""
        this.msg = "Nenhum dado Encontrado!"

        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            if int(codigo) == int(cod):
                this.msg = f"Código: {codigo}, Nome: {nome}, Telefone: {telefone}, Endereco: {endereco}, Data de Nascimento: {dataDeNascimento}"
                return this.msg
        return this.msg

    except Exception as erro:
        return erro

