import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 43568))
print('server is waiting for requests...')

arp_data = {
    '192.168.42.1': 'AE:D3:45:66:7B:55',
    '192.168.42.2': 'AE:D3:46:6D:7C:22'
}


def rarp(query):
    flag = 0
    for key,value in arp_data.items():

        if value == query:
            flag = 1
            return key

    if flag == 0:
        return 'none'


while True:
    msg, addr = server.recvfrom(4096)
    print('RARP request for ', msg.decode(), 'from', addr)
    query = msg.decode()

    result = rarp(query)

    server.sendto(bytes(result, 'utf-8'), addr)

