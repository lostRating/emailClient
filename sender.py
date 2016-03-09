#-*- coding: utf-8 -*-
from core import *
from passwordHidden import *
import base64

def send():
    host = raw_input('please enter your smtp server:\n')
    port = input('please enter the port number (default 25):\n')

    core.initSocket(host, port);
    if (core.feedBack() != 220):
        core.error('connect error')
    core.send('helo ' + host);
    if (core.feedBack() != 250):
        core.error('connect error')
    print 'connect success'

    core.send('auth login');
    if (core.feedBack() != 334):
        core.error('connect error')
    username = raw_input('please enter your username:\n')
    print 'please enter your password:'
    password = pwd_input()
    print
    core.send(base64.b64encode(username))
    if (core.feedBack() != 334):
        core.error('Invalid username')
    core.send(base64.b64encode(password))
    if (core.feedBack() != 235):
        core.error('Password wrong')
    print 'login success'

    mailFrom = raw_input('mail from:\n');
    core.send('mail from:<' + mailFrom + '>')
    if (core.feedBack() != 250):
        core.error('Invalid mail from')
    mailTo = raw_input('mail to:\n');
    core.send('rcpt to:<' + mailTo + '>')
    if (core.feedBack() != 250):
        core.error('Invalid mail to')

    core.send('data')
    if (core.feedBack() != 354):
        core.error('Can not send data')
    subject = raw_input('please input the subject:\n')
    core.send('From: ' + mailFrom)
    core.send('To: ' + mailTo)
    core.send('Subject: ' + subject)
    core.send('')
    print 'enter your email content, ending with a line containing a single dot(.)'
    while True:
        data = raw_input('> ');
        core.send(data)
        if (data == '.'):
            break
    if (core.feedBack() != 250):
        core.error('Fail to send the content')
    else:
        print 'Send success'

    core.close()
