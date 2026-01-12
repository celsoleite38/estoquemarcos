# criar_banco_sqlite.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("🔄 Criando banco SQLite e tabelas...")

from Crud.core import Base, Conexao
from Crud.Models import *

try:
    # Criar engine e tabelas
    db = Conexao()
    Base.metadata.create_all(db.engine)
    
    print("✅ Banco SQLite e tabelas criados!")
    
    # Criar dados iniciais
    session = db.Session()
    
    # Criar níveis
    from Crud.Models import Nivel
    if session.query(Nivel).count() == 0:
        print("📝 Criando níveis...")
        admin = Nivel(nivel='admin')
        usuario = Nivel(nivel='usuario')
        session.add(admin)
        session.add(usuario)
        session.commit()
        print("✅ Níveis criados")
    
    # Criar usuário admin
    from Crud.Models import Usuarios
    if session.query(Usuarios).count() == 0:
        print("👤 Criando usuário admin...")
        admin_user = Usuarios(
            nome='Administrador',
            usuario='admin',
            senha='123456',  # Texto plano
            nivel=1,  # ID do nível admin
            ativo=1,
            cpf='000.000.000-00',
            rg='0000000',
            celular='(00) 00000-0000',
            email='admin@sistema.com',
            cep='00000-000',
            endereco='Rua Principal',
            numero='123',
            bairro='Centro',
            cidade='Cidade',
            estado='SP'
        )
        session.add(admin_user)
        session.commit()
        print("✅ Usuário admin criado")
        print("   👤 Usuário: admin")
        print("   🔑 Senha: 123456")
    
    session.close()
    print("\n🎉 Banco SQLite configurado com sucesso!")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()

input("\nPressione Enter para sair...")