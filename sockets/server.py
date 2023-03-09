import socket
server = socket.socket() 
server.bind(('localhost',7000)) 
server.listen() 

while True:
    client = server.accept()
    reposta = client[0].recv(1024)
    retorno = sum([int(i) for i in str(reposta, 'ascii').split(',')])
    client[0].send(bytes(str(retorno),'ascii'))
    print(''+str(retorno))
