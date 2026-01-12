@echo off
cd /d "D:\controleEstoque-master\controleEstoque-master\controle_estoque"
call venv\Scripts\activate.bat

:: Executa sem console (pythonw)
start "" pythonw main.py

:: Fecha este console imediatamente
exit