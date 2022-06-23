from flask import Flask, render_template, request
import cardapio
import conexao
import operacoes
import this
this.codigo = 0
this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.mensagem = ""


inicio = Flask(__name__) #Representando uma variável do tipo flask

@inicio.route('/', methods=['GET','POST'])
def menu():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.data     = request.form['tNovaData']
        this.dados    = operacoes.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo='Página Principal', resultado=this.dados)

if __name__ == "__main__":
    inicio.run(debug=True, port=5000)
    #conexao.conectar()
    #cardapio.redirecionarCardapio()