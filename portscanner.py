import socket 
ip = input("IP: ")
startport = int(input("Start port: "))
stopport = int(input("Stop port: "))
for ports in range(startport, stopport+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # x = s.connect_ex((ip,ports)) #debug
   # print(x) #debug
    if s.connect_ex((ip, ports)) == 0:
        print ("Port ",ports," Open ")
s.close()
