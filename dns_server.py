import socket
dns_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dns_server.bind(('localhost',153))
print('dns server running on port 153..')
name_servers={
    'google.com':'8.8.8.8'
}

def dns_search(domain):
    flag=0
    for key in name_servers.keys():
        if key==domain:
            return name_servers.get(key)
            flag=1

    if flag==0:
        return 'none'


while True:
    message,addr=dns_server.recvfrom(4096)
    domain=message.decode()
    print('Query from ',addr,'for domain:',message.decode())
    dns_answer=dns_search(domain)
    if dns_answer=='none':
        dns_server.sendto(bytes('Host not found', 'utf8'), addr)

    else:
        dns_server.sendto(bytes(dns_answer, 'utf8'), addr)




