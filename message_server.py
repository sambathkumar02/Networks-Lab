import socket
import sys
import threading
from threading import *

#creating socket object
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#creating mesage server
server.bind(('127.0.0.1',2222))

#limiting sever to 2 conneections
server.listen(2)

#message thread for live messaging
class message(Thread):

    def __init__(self,c1,c2):
        threading.Thread.__init__(self)
        self.sender=c1[0]
        self.reciever=c2[0]

    def run(self):


        while True:
            message = None
            while True:
                while message == None:
                    message = self.sender.recv(4096).decode()
                    print(message)
                self.reciever.send(bytes(message,'utf-8'))
                message=None


connections=0       #for counting connections
details=[]          #storing client objects
while connections<2:
    c,addr=server.accept()
    details.append([c,addr])        #appending client details to single list
    connections+=1


#separating client details
c1=details[0]
c2=details[1]

#Sending Acknowledgements
c1[0].send(bytes('ok','utf-8'))
c2[0].send(bytes('ok','utf-8'))

#creaitng thread objects
client1=message(c1,c2)
client2=message(c2,c1)

#starting threads
client1.start()
client2.start()

#closing connctions
server.close()