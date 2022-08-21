import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serv.bind(("0.0.0.0",4433))
    serv.listen(5)
    print("Aberta")
    
    
    client, addr = serv.accept()
    print(addr[0] + " está conectado")
    
    
    while True:
        data = client.recv(1024).decode()
        print(data)
        if data =="sair\n":
            break
        msg =input("Mensagem: ")+"\n"
        if msg == "sair\n":
            break
        
        client.send(msg.encode())

    serv.close()
except Exception as ex:
    print("erro", ex)
    serv.close()