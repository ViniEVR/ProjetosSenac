import mysql.connector
from mysql.connector import errorcode

def conectar():
    try:
        db_connection = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'bancodedados')
        print('Conectado com sucesso')
        return db_connection

    except mysql.connector.Error as error: #salvando erro na variavel error
        if error.errno == errorcode.ER_BAD_DB_ERROR: #Caso banco de dados não exista
            print('Banco de dados não existe!')

        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:#Caso haja um erro de usuario
            print('Nome de usuario ou senha inválidos!')

        else:
            print(error)

    else:
        db_connectio.close()


