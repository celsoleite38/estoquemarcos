from PyQt5.QtWidgets import QPushButton
from Views.login import Ui_ct_login
from Crud.CrudLogin import Login


class MainLogin(Ui_ct_login):
    def mainlogin(self, frame):
        super(MainLogin, self).setLogin(frame)
        self.frame_login.show()

        # Foco Campos Usuário
        self.tx_user.setFocus()

        global grupo
        grupo = {0: {self.bt_Vendas, self.bt_Clientes},
                 1: {self.bt_Fornecedor,
                     self.bt_MainProdutos, self.bt_Compras},
                 2: {self.bt_Financeiro}, 3: {self.bt_Conf}}

        self.index = {1: self.janelaVendas, 2: self.janelaCompras,
                      3: self.janelaHome, 4: self.janelaHome}

        self.tx_user.returnPressed.connect(self.tx_senha.setFocus)
        self.tx_senha.returnPressed.connect(self.login)
        self.bt_login.clicked.connect(self.login)

    def login(self):
        print(f"🔐 Tentando login - Usuário: {self.tx_user.text()}")
        
        login = Login()
        login.usuario = self.tx_user.text()
        login.senha = self.tx_senha.text()

        print(f"📝 Dados: usuario='{login.usuario}', senha='{login.senha}'")
        
        try:
            if login.logar():
                print(f"✅ Login bem-sucedido!")
                print(f"   ID User: {login.idUser}")
                print(f"   Nome User: {login.nomeUser}")
                print(f"   Nível: {login.nivel}")
                
                self.usuario = login.usuario
                self.senha = login.senha
                self.idUser = login.idUser
                self.userNivel = login.nivel

                # Setando nome de usuário logado
                self.lb_userName.setText(login.nomeUser)
                print(f"👤 Nome setado na interface: {login.nomeUser}")

                # habilitando botoes de acordo com nível
                print(f"🎚️  Habilitando botões para nível {login.nivel}")
                for row in range(login.nivel):
                    for filho in grupo[row]:
                        filho.setVisible(True)

                # Habilitando Botao meus dados e logout
                self.bt_alterSenha.setEnabled(True)
                self.bt_logout.setEnabled(True)

                # Se nivel for menor que 3 desabilita a home
                if self.userNivel < 3:
                    self.bt_Home.setDisabled(True)
                else:
                    self.bt_Home.setEnabled(True)

                print(f"🔄 Redirecionando para índice {login.nivel}...")
                print(f"   Função a ser chamada: {self.index.get(login.nivel)}")
                
                # Tente chamar a função com segurança
                try:
                    func = self.index[login.nivel]
                    print(f"   Chamando {func}...")
                    func()
                    print("✅ Redirecionamento concluído!")
                except Exception as e:
                    print(f"💥 ERRO no redirecionamento: {e}")
                    import traceback
                    traceback.print_exc()
                    
            else:
                print("❌ Login falhou - Credenciais inválidas")
                self.lb_alert.setText("Ops. Algo deu errado. Tente novamente")
                
        except Exception as e:
            print(f"💥 ERRO CRÍTICO no método login(): {e}")
            import traceback
            traceback.print_exc()
            self.lb_alert.setText(f"Erro: {str(e)[:50]}...")