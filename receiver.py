#-*- coding: utf-8 -*-
from core import *
from passwordHidden import *
import base64
import re
from decode import *

def receive():
    host = raw_input('please enter your pop3 server:\n')
    port = input('please enter the port number (default 110):\n')
    
    core.initSocket(host, port)
    if (core.ret().split(' ')[0] != '+OK'):
        core.error('connect error')
    print 'connect success'
    
    username = raw_input('please enter your username:\n')
    print 'please enter your password:'
    password = pwd_input()
    print
    core.send('user ' + username)
    if (core.ret().split(' ')[0][0:3] != '+OK'):
        core.error('Invalid username')
    core.send('pass ' + password)
    if (core.ret().split(' ')[0] != '+OK'):
        core.error('Invalid password')
    print 'login success'

    core.send('stat')
    num = int(core.ret().split(' ')[1])
    print 'You have',num,'mails'
    wanted = input('Enter the number of mails you want to receive: ')
    if (not(0 <= wanted and wanted <= num)):
        core.error('Invalid range')
    core.send('retr ' + str(wanted))
    data = core.ret();
    if (data.split(' ')[0] != '+OK'):
        core.error('Invalid mail number')

    count = 1
    gxx = re.split(' |\n|\r|\n\r', data)
    for i in range(0, len(gxx)):
        if (gxx[i] == '.'):
            count = count - 1
    while count > 0:
        tmp = core.s.recv(1024)
        if tmp:
            data += tmp
            gxx = re.split(' |\n|\r|\n\r', tmp)
            for i in range(0, len(gxx)):
                if (gxx[i] == '.'):
                    count = count - 1
    
    s = re.split('\n|\r|\n\r', data)
    for i in range(0, len(s)):
        if (wanted <= 0):
            break
        if (s[i]):
            print s[i]

    core.close()
