import socket 

client = socket.socket()
client.connect(('localhost',7000))

print('Digite os numeros que voce deseja somar,sendo esses separados por virgula:')

numeros = input('')

client.send(bytes(numeros, 'ascii') )

result = str(client.recv(1024),'ascii') 

print('A soma é:',result)

numeros = ''
    
client.close()
