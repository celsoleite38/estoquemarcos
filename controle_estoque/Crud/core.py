# Crud/core.py - Substitua a classe Conexao
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Conexao(object):
    def __init__(self):
        # Caminho para o banco SQLite na mesma pasta
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, '..', 'sistema.db')
        db_url = f'sqlite:///{db_path}'
        
        print(f"📁 Usando SQLite: {db_path}")
        
        # Engine SQLite
        self.engine = create_engine(db_url, echo=False)
        
        # Criando Sessao
        self.Session = sessionmaker(bind=self.engine)


Base = declarative_base()