import os
from PyQt5 import QtGui

base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, 'controle_estoque', 'Images', 'bg.png')

print(f"Tentando carregar imagem: {image_path}")
image = QtGui.QPixmap(image_path)

if image.isNull():
    print("❌ Falha ao carregar imagem.")
else:
    print("✅ Imagem carregada com sucesso.")
