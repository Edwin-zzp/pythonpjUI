import sys
import socket

import win32api
import win32con
import os
import threading
import time


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from firstUI import Ui_MainWindow

encoding = 'gb2312'





class G:
    port=9999
    stop = True
    BUFSIZE = 1024
    name = ""
    fname = "D:/VIDEO/"

class MyWindow (QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
    def portchange(self):
        G.port = int(myshow.lineEdit.text())
        print(G.port)
    def sendOnClick(self):
        G.stop=False
        lst = Listener(G.port)  # create a listen thread
        lst.start()
    def stopOnClick(self):
        G.stop=True
    def selectOnClick(self,item):
        G.name = item.text()
        print(G.fname)
        print("name="+G.name)
        button = QMessageBox.question(self, "Movie", "你选择了: " + item.text()+"影片\n"+"是否确定？",QMessageBox.Ok|QMessageBox.Cancel,QMessageBox.Ok)
        if button == QMessageBox.Ok:
            G.fname=path+G.name
            os.popen(r"D:/VIDEO/mplayer.exe  -loop 0 -fixed-vo " + G.fname)
        elif button == QMessageBox.Cancel:
            return
        else:
            return


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

# a read thread, read data from remote
class Reader(threading.Thread):
    def __init__(self, client):
        print("Read work")
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        while not G.stop:
            data = self.client.recv(G.BUFSIZE)
            if (data):
                string = bytes.decode(data, encoding)
                print ("from client::", string, "")

                if string == "open":
                    win32api.keybd_event(27, 0, 0, 0)  # ESC
                    time.sleep(0.01)
                    win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)
                    G.fname = path + G.name
                    os.popen(r"D:/VIDEO/mplayer.exe  -loop 0 -fixed-vo " + G.fname)  # -fs
                if string == "pause":
                    win32api.keybd_event(32, 0, 0, 0)  # 空格
                    time.sleep(0.01)
                    win32api.keybd_event(32, 0, win32con.KEYEVENTF_KEYUP, 0)

                if string == "full":
                    win32api.keybd_event(70, 0, 0, 0)  # 输入f
                    time.sleep(0.01)
                    win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
                if string == "send":
                    # self.client.sendall(bytes("你好" + "\n", encoding))
                    # self.client.sendall(bytes("天才" + "\n", encoding))
                    print(len(item))
                    for i in range(0,len(item)):
                        print(item[i])
                        self.client.sendall(bytes(item[i]+"\n",encoding))

                if string == "test":
                    self.client.sendall(bytes("ok" + "\n", encoding))
                #self.client.send("return frome server::" + string)
            else:
                print("close:", self.client.getpeername())
                self.client.shutdown(2)
                self.client.close()
                break




# a listen thread, listen remote connect
# when a remote machine request to connect, it will create a read thread to handle
class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", port))
        self.sock.listen(0)

    def run(self):
        print("listener started")
        while not G.stop:
            client, cltadd = self.sock.accept()
            print("accept a connect...")
            Reader(client).start()
            cltadd = cltadd
            #print(cltadd)
            print("accept a connect(new reader..)")




if __name__=="__main__":

    app=QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()

    ip = get_host_ip()
    #port = "9999"
    #myshow.lineEdit.setText(port)


    myshow.textBrowser.setText(ip)
    myshow.lineEdit.setText(str(G.port))

    item=[]

    path = "D:/VIDEO/"  # 设置路径
    dirs = os.listdir(path)  # 获取指定路径下的文件
    print(dirs)

    for i in dirs :
        if os.path.splitext(i)[1] == ".mp4":
            item.append(i)
    print(item)

    for i in range(0,len(item)):
        myshow.listWidget.addItem(item[i])


    print("watch is show")
    #if(not app.exec()):
    sys.exit(app.exec())

