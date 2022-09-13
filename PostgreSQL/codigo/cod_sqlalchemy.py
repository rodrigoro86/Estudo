from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pprint import pprint

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    pessoa_id = Column(Integer, ForeignKey('pessoa2.id'))
    pessoa = relationship('Pessoa2')

    def __repr__(self):
        return f'Produto(nome={self.nome}, pessoa={self.pessoa})'

class Pessoa2(Base):
    __tablename__ = 'pessoa2'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    produtos = relationship(Produto, backref='pessoa2')

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade}, produtos={self.produtos})'



Base.metadata.create_all(engine)
"""
p1 = Pessoa2(nome='Rodrigo', idade='27')
pd1 = Produto(nome='Livro', pessoa=p1)
pd2 = Produto(nome='CD', pessoa=p1)

session.add_all([pd1, pd2, p1])
session.commit()
p1 = Pessoa2(nome='Eduardo', idade='27')
p2 = Pessoa2(nome='Isaias', idade='30')
p3 = Pessoa2(nome='Olava', idade='40')

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()"""

pprint(session.query(Pessoa2).all())
print(session.query(Produto).filter(Pessoa2.nome=='Rodrigo').first())
print(session.query(Produto).filter_by(nome='CD').filter(Pessoa2.nome=='Rodrigo').all())
"""
p1 = Pessoa(nome = 'Fausto')
p2 = Pessoa(nome = 'Fabio')
p3 = Pessoa(nome = 'Rodrigo')
p5 = Pessoa(nome = 'Teste')

session.add(p1)
session.add_all([p2, p3])

session.commit()

session.add(p5)
session.flush()"""