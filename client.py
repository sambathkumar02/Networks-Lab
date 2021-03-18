import socket

client=socket.socket()

client.connect(('localhost',4444))
while True:
    message=input("Enter mesage for Echo(end to exit):")
    client.send(bytes(message, 'utf-8'))
    if message=='end':
        break
    reply=client.recv(1024).decode()
    print('Reply from server:',reply)

