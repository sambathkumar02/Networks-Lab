import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('localhost',43567))

arp_data={
    '192.168.42.1':'AE:D3:45:66:7B:55',
    '192.168.42.2':'AE:D3:46:6D:7C:22'
}

def arp(query):
    flag = 0
    for key in arp_data.keys():
        if key == query:
            return name_servers.get(key)
            flag = 1

    if flag == 0:
        return 'none'

def rarp(query):
    flag = 0
    for key in arp_data.values():
        if key == query:
            return name_servers.get(key)
            flag = 1

    if flag == 0:
        return 'none'


while True:
    req,addr=server.recvfrom(4096)
    query=req[0]
    protocol=req[1]
    if protocol=='arp':
        result=arp(query)
        server.sendto(bytes('The MAC address:',result),addr)

    else:

        result = rarp(query)
        server.sendto(bytes('The ip address:', result), addr)

