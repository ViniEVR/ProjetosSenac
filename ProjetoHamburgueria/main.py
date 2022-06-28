from flask import Flask, render_template, request
import this
import cardapio
import conexao
import operacoes
this.codigo = 0
this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.mensagem = ""
this.lanche = ""
this.ingredienteLanche = ""
this.valorLanche = 0


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

@inicio.route('/funcionario.html', methods = ['GET', 'POST'])
def menuFuncionario():
    if request.method == 'POST':
        this.lanche = request.form['cLanche']
        this.ingredienteLanche = request.form['cIngredienteLanche']
        this.valorLanche = float(request.form['cValorLanche'])
        this.dados = operacoes.inserirLanches(this.lanche, this.ingredienteLanche, this.valorLanche)
    return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)

@inicio.route('/teste.html', methods = ['GET', 'POST'])
def testinho():
    if request.method == 'POST':
        this.lanche = request.form['cLanche']
        this.ingredienteLanche = request.form['cIngredienteLanche']
        this.valorLanche = request.form['cValorLanche']
        this.dados = operacoes.inserirLanches(this.lanche, this.ingredientes, float(this.valorLanche))
    return render_template('teste.html', titulo='Funcionário - ADM', resultado=this.dados)


if __name__ == "__main__":
    inicio.run(debug=True, port=5000)
    conexao.conectar()
    #cardapio.redirecionarCardapio()