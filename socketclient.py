#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
port=9999
host='192.168.2.152'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.connect((host,port))
except:
    print('连接错误！')


#data=input('输入要发送的信息：').strip()
data="stop"
s.send(bytes(data, encoding='utf8'))
#s.shutdown(1)
print('发送完成。')
while 1:
    buf=s.recv(4096)
    if not len(buf):
        break
    print(buf)
    s.shutdown(1)