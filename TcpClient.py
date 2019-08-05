# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:17:50 2018

@author: YJIANG14
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 3333))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))         
s.send(b'exit')
s.close()

            
        
    