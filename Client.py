import socket

s = socket.socket()
host = socket.gethostname()
port = 8082
data = ''
s.connect(('71.9.176.217',port))
while 1:
    data = s.recv(512)
    if ( data == 'q' or data == 'Q'):
        s.close()
        break
    else:
        print "RECIEVED:" , data
        data = raw_input ( "SEND( TYPE q or Q to Quit):" )
        if (data <> 'Q' and data <> 'q'):
            s.send(data)
        else:
            s.send(data)
            s.close()
            break
