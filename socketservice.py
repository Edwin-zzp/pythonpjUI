#!/usr/bin/env python
# -*- coding: utf-8 -*-
##tcp响应服务器，当与客户端建立连接后，服务器显示客户端ip和端口，同时将接收的客户端信息和'I get it!'传给客户端，此时等待输入一个新的信息传给客户端。

import socket,traceback
import os#, sys
import time

import win32api
import win32con

fname="D:/VIDEO/12.mp4"
fn="12.mp4"

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

host=get_host_ip();
#host='192.168.1.27'
port=9999

print(host)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port))
s.listen(2)

while 1:
    try:
        clientsock,clientaddr=s.accept()
        print("连接来自：", clientsock.getpeername())
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    try:
        while 1:
            data = clientsock.recv(4096)
            if not len(data):
                time.sleep(2)
                break
            #print(str(clientsock.getpeername()[0]+':'+str(data)))
            print(data)
            if data==b"open":
                win32api.keybd_event(27, 0, 0, 0)  # ESC
                time.sleep(0.01)
                win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)
                os.popen(r"D:/VIDEO/mplayer.exe  -loop 0 -fixed-vo " + fname)  # -fs
            if data==b"pause":
                win32api.keybd_event(32, 0, 0, 0)  #空格
                time.sleep(0.01)
                win32api.keybd_event(32, 0, win32con.KEYEVENTF_KEYUP, 0)
            #clientsock.sendall(data)
            if data==b"full":
                win32api.keybd_event(70, 0, 0, 0)  # 输入f
                time.sleep(0.01)
                win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
            if data==b"send":
                clientsock.sendall(bytes("你好"+"\n",encoding='utf8'))
                clientsock.sendall(bytes("天才"+"\n", encoding='utf8'))

            #clientsock.sendall(bytes("你好"+"\n", encoding='utf8'))
            #t=input('input the word:')
            #clientsock.sendall(bytes(t, encoding='utf8'))
    except (KeyboardInterrupt,SystemExit):
        raise
    except:

        traceback.print_exc()

    try:
        print("connect close  ")
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()