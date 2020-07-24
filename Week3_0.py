import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.srmist.edu.in',80))
cmd='GET https://www.srmist.edu.in/content/gateway-student\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data=mysock.recv(600)
    if(len(data)<1):
     break
    else:
     print(data.decode())
mysock.close()
