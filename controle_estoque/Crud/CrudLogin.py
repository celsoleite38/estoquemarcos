# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_


from Crud.core import Conexao
from Crud.Models import Usuarios


class Login(object):

    def __init__(self, usuario="", senha="", idUser="", nomeUser="", nivel="",
                 validar=""):

        self.usuario = usuario
        self.senha = senha
        self.idUser = idUser
        self.nomeUser = nomeUser
        self.nivel = nivel

    def logar(self):
        print(f"🔍 Verificando no banco: usuario='{self.usuario}', senha='{self.senha}'")
        print("="*50)
        
        self.validar = False
        self.idUser = ""
        self.nomeUser = ""
        self.nivel = ""

        try:
            # Conexão DIRETA - método mais seguro
            from sqlalchemy import text
            
            print("1. Criando conexão...")
            conecta = Conexao()
            
            print("2. Abrindo conexão direta...")
            with conecta.engine.connect() as conn:
                print("3. Conexão estabelecida")
                
                # Query SIMPLES e DIRETA
                sql = text("""
                    SELECT id, nome, usuario, senha, nivel 
                    FROM usuario 
                    WHERE usuario = :usuario 
                    AND senha = :senha 
                    AND ativo = 1
                    LIMIT 1
                """)
                
                print(f"4. Executando query para usuário '{self.usuario}'...")
                result = conn.execute(sql, {
                    'usuario': self.usuario, 
                    'senha': self.senha
                })
                
                row = result.fetchone()
                
                if row:
                    print("🎉✅ USUÁRIO ENCONTRADO!")
                    print(f"   ID: {row[0]}")
                    print(f"   Nome: {row[1]}")
                    print(f"   Usuário: {row[2]}")
                    print(f"   Nível: {row[4]}")
                    
                    self.validar = True
                    self.idUser = row[0]      # id
                    self.nomeUser = row[1]    # nome
                    self.usuario = row[2]     # usuario
                    self.senha = row[3]       # senha
                    self.nivel = row[4]       # nivel
                else:
                    print("❌ Nenhum usuário encontrado com essas credenciais")
                    
            print("✅ Conexão fechada")

        except Exception as err:
            print(f"💥💥💥 ERRO CRÍTICO no login: {err}")
            import traceback
            traceback.print_exc()
            self.validar = False

        print(f"📤 Retornando: validar={self.validar}")
        print("="*50)
        return self.validar