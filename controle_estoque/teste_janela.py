from PyQt5 import QtWidgets
import sys

class Teste(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela de Teste")
        self.resize(600, 400)
        self.move(200, 200)

        label = QtWidgets.QLabel("Janela funcionando!", self)
        label.setStyleSheet("font-size: 20px; color: green;")
        label.adjustSize()  # 🔧 ajusta o tamanho do label ao conteúdo
        label.move(50, 50)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela = Teste()
    janela.show()
    sys.exit(app.exec_())
