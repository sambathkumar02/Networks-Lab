import socket

server=socket.socket()
server.bind(('localhost',4444))
server.listen(1)
print('Listening for connection.....')
while True:
    client,address=server.accept()
    print('connected with',client)
    message=client.recv(1024).decode()
    while message!='end':
        client.send(bytes(message,'utf-8'))
        message = client.recv(1024).decode()
    client.close()
    break



