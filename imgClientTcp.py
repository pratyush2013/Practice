import socket
import base64
import struct

def send(socket,msg):
    msg=struct.pack(">I",len(msg))+msg
    
    socket.sendall(msg)

def recieve(sock):
    packObj=recieve_helper(sock,4)          # pack object is always of 4 byte
    length=struct.unpack(">I",packObj)[0]   # Big-Endian struct unpack return tuple so [0] returns 1st obj in tuple
    if length == 0:
        return
    return recieve_helper(sock,length-4)    #-4 bytes for previously returned 4
    

def recieve_helper(sock,n):
    data=''
    while len(data)<n:
        packet=sock.recv(n-len(data))
        data+=packet            
    return packet


client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address=("localhost",1024)
client_sock.connect(address)

pngFile=open("1.png","rb")
string=base64.b64encode(pngFile.read())
part=0
send(client_sock,string)
f=open("copid1.png","ab+")
f.write(recieve(client_sock)) 
f.close()
client_sock.close()









