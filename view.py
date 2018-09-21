# -*- coding: UTF-8 -*-
import os#, sys
import time

import win32api
import win32con
#import win32gui
#from ctypes import *


fname="D:/VIDEO/12.mp4"
fn="12.mp4"
#print(fn)
#print(fname)
#os.system(r"D:/VIDEO/mplayer.exe -fs -loop 0 -fixed-vo " + fname)
os.popen(r"D:/VIDEO/mplayer.exe  -loop 0 -fixed-vo " + fname)   #-fs

time.sleep(2)

win32api.keybd_event(32,0,0,0)
time.sleep(0.01)
win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0)

