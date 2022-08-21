import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

try:
    while True:
        msg = input("Menssagem:" ) + "\n"
        if msg=="sair\n":
            break
        client.sendto(msg.encode(),("192.168.15.2",444))
        data, sender = client.recvfrom(1024)
        print(sender[0]+": "+ data.decode())
        if data.decode()=="sair\n":
            break
    client.close()
except Exception as Erro:
    print("Erro no envio" + Erro)