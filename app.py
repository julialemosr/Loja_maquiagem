from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from models import Cliente, Produto, Venda, db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def inicio():
    return render_template('base.html')


@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    sql_clientes = select(Cliente)
    resultado_clientes = db_session.execute(sql_clientes).scalars()
    lista_clientes = []
    for n in resultado_clientes:
        lista_clientes.append(n.serialize_cliente())
        print(lista_clientes[-1])
    return render_template("lista_cliente.html",
                           lista_clientes=lista_clientes)


@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    sql_produtos = select(Produto)
    resultado_produtos = db_session.execute(sql_produtos).scalars()
    lista_produtos = []
    for n in resultado_produtos:
        lista_produtos.append(n.serialize_produto())
        print(lista_produtos[-1])
    return render_template("lista_produto.html",
                           lista_produtos=lista_produtos)


@app.route('/vendas', methods=['GET', 'POST'])
def vendas():
    sql_vendas = select(Venda)
    resultado_vendas = db_session.execute(sql_vendas).scalars()
    lista_vendas = []
    for n in resultado_vendas:
        lista_vendas.append(n.serialize_venda())
        print(lista_vendas[-1])
    return render_template("lista_venda.html",
                           lista_vendas=lista_vendas)


@app.route('/novo_cliente', methods=['POST', 'GET'])
def criar_clientes():
    if request.method == "POST":
        if not request.form['form-CPF']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-Nome']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-telefone']:
            flash("Preencher todos os campos!! ", "error")

        else:
            form_evento = Cliente(CPF=str(request.form['form-CPF']),
                                  Nome=str(request.form['form-Nome']),
                                  telefone=str(request.form['form-telefone'])
                                  )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("CLIENTE ADICIONADO COM SUCESSO!!", "success")
            return redirect(url_for('clientes'))

    return render_template('novo_cliente.html')


@app.route('/novo_produto', methods=['POST', 'GET'])
def criar_produtos():
    if request.method == "POST":
        if not request.form['form-valor_produto']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-nome_produto']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-quantidade_estoque']:
            flash("Preencher todos os campos!! ", "error")

        else:
            form_evento = Produto(valor_produto=float(request.form['form-valor_produto']),
                                  nome_produto=str(request.form['form-nome_produto']),
                                  quantidade_estoque=int(request.form['form-quantidade_estoque'])
                                  )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("PRODUTO ADICIONADO COM SUCESSO!!", "success")
            return redirect(url_for('produtos'))

    return render_template('novo_produto.html')


@app.route('/nova_venda', methods=['POST', 'GET'])
def criar_vendas():
    if request.method == "POST":
        print('vendasInicio')
        if not request.form['form-data']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-valor_final']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-quantidade_produto']:
            flash("Preencher todos os campos!! ", "error")

        else:
            form_evento = Venda(data=str(request.form['form-data']),
                                valor_final=float(request.form['form-valor_final']),
                                quantidade_produto=int(request.form['form-quantidade_produto']),
                                id_produto1=int(request.form['form-id_produto']),
                                id_cliente1=int(request.form['form-id_cliente'])
                                )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("VENDA ADICIONADA COM SUCESSO!!", "success")
            return redirect(url_for('vendas'))

    return render_template('nova_venda.html')


if __name__ == '__main__':
    app.run(debug=True)
