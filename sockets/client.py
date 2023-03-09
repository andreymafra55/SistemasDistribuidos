import socket 

client = socket.socket()
client.connect(('10.35.4.90',7000))

print('digite os numeros que deseja somar separados por virgula')

numeros = input('')

client.send(bytes(numeros, 'ascii') )

result = str(client.recv(1024),'ascii') 

print('A soma é:',result)

numeros = ''
    
client.close()
