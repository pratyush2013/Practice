import socket
import struct
def send(sock,msg):
    msg=struct.pack(">I",len(msg))+msg
    print type(msg)
    sock.sendall(msg)

def recieve(sock):
    packObj=recieve_helper(sock,4)
    length=struct.unpack(">I",packObj)[0]
    if length == 0:
        return
    return recieve_helper(sock,length-4)
    

def recieve_helper(sock,n):
    data=''
    while len(data)<n:
        packet=sock.recv(n-len(data))
        data+=packet            
    return packet

MAX_BYTES = 65535

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",1024))
sock.listen(10)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
while True:
   
    client_sock,address=sock.accept()
    data=recieve(client_sock)
   
    print "Gotcha",data
    send(client_sock,data)
    print "If you want to establish another connection press"
    a=raw_input()
    if a!='y' and a!='Y':
        break





