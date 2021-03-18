import socket

client=socket.socket()
server=('saranathan.ac.in',80)
client.connect(server)

header = b'GET / HTTP/1.1\r\n'
header += b'Host: saranathan.ac.in:80\r\n'
header += b'Accept:text/html\r\n'
header += b'Connection: close\r\n'
header += b'\r\n'

client.send(header)

response=b''


while True:
    buffer=client.recv(4096)
    if not buffer:
        break
    response +=buffer

print(response.decode())
client.close()