# encoding: utf-8
import os,sys

path = "/Users/zhang/Desktop/pythonpj"                           # 设置路径
dirs = os.listdir(path)        # 获取指定路径下的文件


for i in dirs:                             # 循环读取路径下的文件并筛选输出
    if os.path.splitext(i)[1] == ".py":   # 筛选 文件
        print (i)                          # 输出所有的 文件