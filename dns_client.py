import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
domain_name=input('Enter host name:')
client.sendto(bytes(domain_name,'utf-8'),('localhost',153))
result=client.recvfrom(4096)
print('The ip address:',result[0].decode())