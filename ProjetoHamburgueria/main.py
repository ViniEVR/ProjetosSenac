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
this.valorBebida = 0
this.bebida = ""
this.cadastro = ""
this.ingredienteSobremesa = ""
this.valorSobremesa = 0
this.sobremesa = ""
this.Funcionario = ""
this.senhaFuncionario = ""


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
        if request.form['cadastrar']  == "1":
            this.lanche = request.form['cLanche']
            this.ingredienteLanche = request.form['cIngredienteLanche']
            this.valorLanche = float(request.form['cValorLanche'])
            this.dados = operacoes.inserirLanches(this.lanche, this.ingredienteLanche, this.valorLanche)
            return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)
        elif request.form['cadastrar']  == '2':
            this.codigo = request.form['cCodigo']
            this.dados = operacoes.excluirLanche(this.codigo)
            return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados) 
        elif  request.form['cadastrar'] == '3':
            this.bebida = request.form['cBebida']
            this.valorBebida = request.form['cValorBebida']
            this.dados = operacoes.inserirBebidas(this.bebida, float(this.valorBebida))
            return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)
        elif request.form['cadastrar']  == '4':
            this.codigo = request.form['cCodigo']
            this.dados = operacoes.excluirBebida(this.codigo)
            return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)    
        elif  request.form['cadastrar'] == '5':
            this.sobremesa = request.form['cSobremesa']
            this.ingredienteSobremesa = request.form['cIngredienteSobremesa']
            this.valorSobremesa = float (request.form['cValorSobremesa'])
            this.dados = operacoes.inserirSobremesas(this.sobremesa, this.ingredienteSobremesa, this.valorSobremesa)
            return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)
        elif request.form['cadastrar']  == '6':
            this.codigo = request.form['cCodigo']
            this.dados = operacoes.excluirSobremesa(this.codigo)
            return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)              
        elif  request.form['cadastrar'] == '7':
            this.Funcionario = request.form['cFuncionario']
            this.senhaFuncionario = request.form['cSenhaFuncionario']
            this.dados = operacoes.inserirFuncionario(this.Funcionario, this.senhaFuncionario)
            return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)  
        elif request.form['cadastrar']  == '8':
            this.codigo = request.form['cCodigo']
            this.dados = operacoes.excluirFuncionario(this.codigo)
            return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)        
        else:
            return render_template('notFound.html')
    return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)
    
def cadastroBebida():
    if request.method == 'POST':
        this.bebida = request.form['cBebida']
        this.valorBebida = request.form['cValorBebida']
        this.dados = operacoes.inserirBebidas(this.bebida, float(this.valorBebida))
    return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)


@inicio.route('/teste.html', methods = ['GET', 'POST'])
def cadastroBebida():
    if request.method == 'POST':
        this.bebida = request.form['cBebida']
        this.valorBebida = request.form['cValorBebida']
        this.dados = operacoes.inserirBebidas(this.bebida, float(this.valorBebida))
    return render_template('teste.html', titulo='Funcionário - ADM', resultado=this.dados)


if __name__ == "__main__":
    inicio.run(debug=True, port=5000)
    conexao.conectar()
    #cardapio.redirecionarCardapio()