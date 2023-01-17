Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
... 
... # Limpar cache DNS
... os.system('ipconfig /flushdns')
... 
... # Limpar arquivos temporários
... os.system('rd /s /q %temp%')
... 
... # Renovar conexão de rede
... os.system('ipconfig /renew')
... 
... # Reiniciar políticas de rede
... os.system('netsh int ip reset')
