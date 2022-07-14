from flask import Flask, render_template, request
import this

from numpy import character
import cardapio
import conexao
import operacoes
import re
this.flag = False
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
this.nDado = ""
this.dado = ""



inicio = Flask(__name__) #Representando uma variável do tipo flask

@inicio.route('/', methods=['GET','POST'])
def menu():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.ingredientes = request.form['ingredientes']
        this.preco = request.form['preco']
        this.data     = request.form['tNovaData']
        this.dados    = operacoes.inserir(this.nome, this.ingredientes, this.preco, this.data)
    return render_template('index.html', titulo='Página Principal', resultado=this.dados)


@inicio.route('/funcionario.html', methods = ['GET', 'POST'])
def menuFuncionario():
    if request.method == 'POST':
        this.codigo = operacoes.selecionarCodigoLanche()
        this.nome = operacoes.selecionarNomeLanche()
        this.ingrediente = operacoes.selecionarIngredienteLanche()
        this.valor = operacoes.selecionarValorLanche()
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
    return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados, len = len(this.codigo), codigo = this.codigo, nome = this.nome, ingrediente = this.ingrediente, valor = this.valor)
    
def cadastroBebida():
    if request.method == 'POST':
        this.bebida = request.form['cBebida']
        this.valorBebida = request.form['cValorBebida']
        this.dados = operacoes.inserirBebidas(this.bebida, float(this.valorBebida))
    return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)
 


@inicio.route('/cardapio.html', methods = ['GET', 'POST'])
def teste():

        if request.method == 'POST':
            this.codigo = operacoes.selecionarCodigoLanche()
            this.nome = operacoes.selecionarNomeLanche()
            this.ingrediente = operacoes.selecionarIngredienteLanche()
            this.valor = operacoes.selecionarValorLanche()
 
        
        return render_template('cardapio.html', titulo = 'Cardápio', len = len(this.codigo), codigo = this.codigo, nome = this.nome, ingrediente = this.ingrediente, valor = this.valor)


@inicio.route('/atualizar.html', methods=['GET','POST'])
def atualizarDados():
    if request.method == 'POST':
        if request.form['atualizar']  == '1':
            this.codigo = request.form['tCodigo']
            this.campo = request.form['tCampo']
            this.nDado  = request.form['tNovoDado']
            this.dado = operacoes.atualizar(this.codigo, this.campo, this.nDado)
            return render_template('funcionario.html', titulo='Atualizar', resultado=this.dado)
        elif request.form['atualizar']  == '2':
            this.codigo = request.form['tCodigo']
            this.campo  = request.form['tCampo']
            this.nDado  = request.form['tNovoDado']
            this.dado = operacoes.atualizarBebida(this.codigo, this.campo, this.nDado)
            return render_template('funcionario.html', titulo='Atualizar', resultado=this.dado)
        elif request.form['atualizar']  == '3':
            this.codigo = request.form['tCodigo']
            this.campo  = request.form['tCampo']
            this.nDado  = request.form['tNovoDado']
            this.dado = operacoes.atualizarSobremesa(this.codigo, this.campo, this.nDado)
            return render_template('funcionario.html', titulo='Atualizar', resultado=this.dado)
        elif request.form['atualizar']  == '4':
            this.codigo = request.form['tCodigo']
            this.campo  = request.form['tCampo']
            this.nDado  = request.form['tNovoDado']
            this.dado = operacoes.atualizarFuncionario(this.codigo, this.campo, this.nDado)
            return render_template('funcionario.html', titulo='Atualizar', resultado=this.dado)
        else:
            return render_template('notFound.html')
    return render_template('funcionario.html', titulo='Funcionário - ADM', resultado=this.dados)


if __name__ == "__main__":
    inicio.run(debug=True, port=5000)
    conexao.conectar()
    #cardapio.redirecionarCardapio()