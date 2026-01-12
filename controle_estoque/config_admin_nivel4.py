# config_admin_nivel4.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Crud.core import Conexao
from Crud.Models import Usuarios, Nivel

print("⚙️ Configurando admin como nível 4 (máximo)...")

db = Conexao()
session = db.Session()

try:
    # 1. Verificar/Criar todos os níveis necessários
    print("📊 Verificando níveis...")
    
    niveis_necessarios = [
        (1, 'vendedor'),
        (2, 'gerente'),
        (3, 'supervisor'),
        (4, 'administrador')  # Nível máximo
    ]
    
    for id_nivel, nome in niveis_necessarios:
        nivel = session.query(Nivel).filter(Nivel.id == id_nivel).first()
        if not nivel:
            print(f"   Criando nível {id_nivel}: '{nome}'")
            nivel = Nivel(id=id_nivel, nivel=nome)
            session.add(nivel)
    
    session.commit()
    print("✅ Níveis configurados")
    
    # 2. Atualizar admin para nível 4
    print("\n👤 Buscando usuário admin...")
    admin = session.query(Usuarios).filter(Usuarios.usuario == 'admin').first()
    
    if admin:
        print(f"   Encontrado: {admin.nome} (nível atual: {admin.nivel})")
        
        if admin.nivel != 4:
            admin.nivel = 4
            session.commit()
            print(f"   ✅ Admin atualizado para nível 4 (administrador)")
        else:
            print(f"   ✅ Admin já está no nível 4")
            
        # Verificar detalhes
        nivel_admin = session.query(Nivel).filter(Nivel.id == 4).first()
        print(f"   🏷️  Nível: {nivel_admin.nivel if nivel_admin else 'N/A'}")
        print(f"   ✅ Ativo: {admin.ativo}")
        
    else:
        print("❌ Usuário admin não encontrado")
        print("   Criando novo admin nível 4...")
        
        admin = Usuarios(
            nome='Administrador',
            usuario='admin',
            senha='123456',
            nivel=4,
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
        session.add(admin)
        session.commit()
        print("   ✅ Admin criado com nível 4")
    
    # 3. Listar todos os usuários para verificação
    print("\n📋 Todos os usuários no sistema:")
    usuarios = session.query(Usuarios).all()
    for user in usuarios:
        nivel_nome = session.query(Nivel).filter(Nivel.id == user.nivel).first()
        print(f"   👤 {user.usuario}: {user.nome} (Nível {user.nivel} = '{nivel_nome.nivel if nivel_nome else 'N/A'}')")
    
    session.close()
    
    print("\n" + "="*50)
    print("🎉 CONFIGURAÇÃO CONCLUÍDA!")
    print("="*50)
    print("Credenciais para login:")
    print("👤 Usuário: admin")
    print("🔑 Senha: 123456")
    print("🏷️  Nível: 4 (Administrador - Acesso total)")
    print("\nReinicie o programa para aplicar as mudanças.")
    
except Exception as e:
    print(f"💥 Erro: {e}")
    import traceback
    traceback.print_exc()
    session.rollback()

input("\nPressione Enter para sair...")