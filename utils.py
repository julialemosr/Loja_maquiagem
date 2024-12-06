from models import Cliente, Produto, Venda, db_session
from sqlalchemy import select


def inserir_cliente():
    cliente = Cliente(Nome=str(input('Nome do cliente: ')),
                    CPF=str(input('CPF do cliente: ')),
                    telefone=str(input('Telefone do cliente: '))
                    )
    print(cliente)
    cliente.save()


def consultar_cliente():
    var_cliente = select(Cliente)
    var_cliente = db_session.execute(var_cliente).all()
    print(var_cliente)


def atualizar_cliente():
    var_cliente = select(Cliente).where(Cliente.Nome == str(input('Nome do cliente: ')) == Cliente.Nome)
    var_cliente = select(Cliente).where(Cliente.CPF == str(input('CPF do cliente: ')) == Cliente.CPF)
    var_cliente = select(Cliente).where(Cliente.telefone == str(input('Telefone do cliente: ')) == Cliente.telefone)
    var_cliente = db_session.execute(var_cliente).scalar()
    print(var_cliente)
    var_cliente.Nome = str(input('Novo nome do cliente: '))
    var_cliente.CPF = str(input('Novo CPF do cliente: '))
    var_cliente.telefone = str(input('Novo telefone do cliente: '))
    var_cliente.save()


def deletar_cliente():
    cliente_deletar = input('Qual cliente você deseja deletar? ')
    var_cliente = select(Cliente).where(cliente_deletar == Cliente.Nome2)
    var_cliente = db_session.execute(var_cliente).scalar()
    var_cliente.delete()




def inserir_produto():
    produto = Produto(valor_produto=float(input('Valor do produto: ')),
                    nome_produto=str(input('Nome do produto: ')),
                    quantidade_estoque=int(input('Quantidade de produto no estoque: '))
                    )
    print(produto)
    produto.save()


def consultar_produto():
    var_produto = select(Produto)
    var_produto = db_session.execute(var_produto).all()
    print(var_produto)

def atualizar_produto():
    var_produto = select(Produto).where(Produto.valor_produto == float(input('Valor do produto: ')) == Produto.valor_produto)
    var_produto = select(Produto).where(Produto.nome_produto == str(input('Nome do produto: ')) == Produto.nome_produto)
    var_produto = select(Produto).where(Produto.quantidade_estoque == int(input('Quantidade de produto no estoque: ')) == Produto.quantidade_estoque)
    var_produto = db_session.execute(var_produto).scalar()
    print(var_produto)
    var_produto.valor_produto = float(input('Novo valor do produto: '))
    var_produto.nome_produto = str(input('Novo nome do produto: '))
    var_produto.quantidade_estoque = int(input('Nova quantidade de produto no estoque: '))
    var_produto.save()


def deletar_produto():
    produto_deletar = input('Qual produto você deseja deletar? ')
    var_produto = select(Produto).where(produto_deletar == Produto.nome_produto)
    var_produto = db_session.execute(var_produto).scalar()
    var_produto.delete()



def inserir_venda():
    venda = Venda(data=int(input('Qual a data da venda: ')),
                  valor_final=float(input('Valor da venda: ')),
                  quantidade_produto=int(input('Quantidade de produto que foi comprado: '))
                  )
    print(venda)
    venda.save()


def consultar_venda():
    var_venda = select(Venda)
    var_venda = db_session.execute(var_venda).all()
    print(var_venda)

def atualizar_venda():
    var_venda = select(Venda).where(Venda.data == int(input('Data da venda: ')) == Venda.data)
    var_venda = select(Venda).where(Venda.valor_final == float(input('Valor final da compra: ')) == Venda.valor_final)
    var_venda = select(Venda).where(Venda.quantidade_produto == int(input('Quantidade de produto vendido: ')) == Venda.quantidade_produto)
    var_venda = db_session.execute(var_venda).scalar()
    print(var_venda)
    var_venda.data = int(input('Nova data da venda: '))
    var_venda.valor_final= float(input('Novo valor final da compra: '))
    var_venda.quantidade_produto = int(input('Nova quantidade de produto vendido '))
    var_venda.save()


def deletar_venda():
    venda_deletar = input('Qual venda você deseja deletar? ')
    var_venda = select(Venda).where(venda_deletar == Venda.id_venda)
    var_venda = db_session.execute(var_venda).scalar()
    var_venda.delete()