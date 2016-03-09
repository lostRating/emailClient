#-*- coding: utf-8 -*-
import socket
import ssl

class core():
    s = socket.socket()

    @staticmethod
    def error(msg):
        core.close()
        assert False

    @staticmethod
    def ret():
        tmp = core.s.recv(1024);
        return tmp

    @staticmethod
    def feedBack():
        return int(core.s.recv(1024).split(' ')[0])
    
    @staticmethod
    def initSocket(host, port):
        core.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        core.s.connect((host, port))

    @staticmethod
    def send(msg):
        core.s.send(msg + '\r\n')

    @staticmethod
    def close():
        core.s.close()
        
