from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base
engine = create_engine('sqlite:///base_loja_maquiagem.sqlite3')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Cliente(Base):
    __tablename__ = 'CLIENTES'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    CPF = Column(String(11), nullable=False, index=True, unique=True)
    Nome = Column(String(40), nullable=False, index=True)
    telefone = Column(String(20), nullable=False, index=True)

    def __repr__(self):
        return '<Cliente: {} {} {} {} '.format(self.id_cliente, self.CPF, self.Nome, self.telefone)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_cliente(self):
        dados_cliente = {
            "id_cliente": self.id_cliente,
            "CPF": self.CPF,
            "Nome": self.Nome,
            "telefone": self.telefone
        }
        return dados_cliente



class Produto(Base):
    __tablename__ = 'PRODUTO'
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    valor_produto = Column(Float, nullable=False, index=True)
    nome_produto = Column(String(40), nullable=False, index=True)
    quantidade_estoque = Column(Integer, nullable=False, index=True)
    def __repr__(self):
        return '<Produto: {} {} {} {}'.format(self.id_produto, self.valor_produto, self.nome_produto, self.quantidade_estoque)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_produto(self):
        dados_produto = {
            "id_produto": self.id_produto,
            "valor_produto": self.valor_produto,
            "nome_produto": self.nome_produto,
            "quantidade_estoque": self.quantidade_estoque
        }
        return dados_produto


class Venda(Base):
    __tablename__ = 'VENDA'
    id_venda = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String, nullable=False)
    valor_final = Column(Float, nullable=False, index=True)
    quantidade_produto = Column(Integer, nullable=False, index=True)
    id_produto1 = Column(Integer, ForeignKey('PRODUTO.id_produto'), nullable=False)
    produto = relationship('Produto')
    id_cliente1 = Column(Integer, ForeignKey('CLIENTES.id_cliente'), nullable=False)
    cliente = relationship('Cliente')

    def __repr__(self):
        return '<Venda: {} {} {} '.format(self.id_venda, self.valor_final, self.quantidade_produto)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_venda(self):
        dados_venda = {
            "id_venda": self.id_venda,
            "valor_final": self.valor_final,
            "quatidade_produto": self.quantidade_produto,
            'id_cliente': self.id_cliente1,
            'id_produto1': self.id_produto1
        }
        return dados_venda

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()