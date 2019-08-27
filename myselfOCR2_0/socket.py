# #!/usr/bin/env python
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'
from socket import *

import myselfOCR.fileOpera as fileOpera


HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection......')
    tcpCliSock, addr = tcpSerSock.accept()
    print( '...connected from:', addr)
    #读取数据 并它保存起来

    tmp=b''

    while 1:
        data = tcpCliSock.recv(BUFSIZ)
        tmp = tmp+data
        if not data:
            break
    tcpCliSock.close()
    fileOpera.writeByteFile("tmp.JPEG", tmp)
tcpSerSock.close()




