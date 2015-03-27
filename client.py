#!/usr/bin/python
#coding:utf-8
import socket
#HOST = '111.206.45.12'
HOST = '127.0.0.1'
PORT = 27277
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    command = raw_input('Input your linux command: ')
    if command == 'quit':
        break
    if not command:
    	break
    s.send(command)
    data = s.recv(10240)#.decode('utf-8')
    if not data:
    	break
    print data
s.close()
