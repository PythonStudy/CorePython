from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_IMET,SOCK_STREAM)
sockobj.bind((myHost,myPort))
sockobj.listen(5)

while True:
    connection,address = sockobj.accept()
    print('Server Connected by',address)
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(b'Echo=>' + data)
    connection.close()
