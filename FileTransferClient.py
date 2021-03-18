import socket

client=socket.socket()
client.connect(('localhost',4445))

f=open('result.html','wb')

data=client.recv(4096)
while data:
    f.write(data)
    data = client.recv(4096)

print('File Recieved Sucessfully..')
f.close()
client.close()



