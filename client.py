from sender import *
from receiver import *

def client():
    print 'Welcome to the simple email client'
    print 'You can type help command for more information'
    while True:
        c = raw_input('> ')
        if (c == 'help'):
            print 'There are following commands:'
            print 'help'
            print 'send'
            print 'receive'
            print 'quit'
        else:
            if (c == 'send'):
                send()
                break
            else:
                if (c == 'receive'):
                    receive()
                    break
                else:
                    if (c == 'quit'):
                        break
                    else:
                        print 'unknown command'

client()
