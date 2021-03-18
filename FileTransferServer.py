import socket

server=socket.socket()
server.bind(('localhost',4445))
server.listen(1)
print('listening..')

while True:
    client,addr=server.accept()
    print('connection Established')
    f=open('index.html','rb')
    data=f.read(4096)
    while data:
        client.send(data)
        data=f.read(4096)
    print('File Transfered Sucessfully..')
    f.close()
    client.close()
    break

