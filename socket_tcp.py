import socket #importando Socket


try:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Criando Socket, Argumento: Familia - IPV4, Argumento 2: Protocolo - TCP

    client.connect(("192.168.15.9", 4433)) #Metodo para conexão
    
    while True:
        msg =input("Mensagem: ") +"\n".encode
        if msg == "exit\n": #Caso a Menssagem for exit ele para a comunicação
            break
        client.send(msg)#Enviado dados
        pacote = client.recv(1024).decode()#Recebe 
        print(pacote)

    client.close()
except Exception as ex:
    print("Erro " + ex)