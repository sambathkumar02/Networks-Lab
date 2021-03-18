import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
arp_server=('localhost',43567)
rarp_server=('localhost',43568)


while True:
    protocol=input("Enter type(arp/rarp):")
    if  (protocol == 'arp' or protocol == 'rarp'):
        break
    else:
        print('Enter correct option..')



if protocol=='arp':
    query=input('Enter ip:')
    client.sendto(bytes(query,'utf-8'),arp_server)
else:
    query = input('Enter MAC:')
    client.sendto(bytes(query,'utf-8'),rarp_server)

result=client.recvfrom(4096)

print(result[0].decode())

