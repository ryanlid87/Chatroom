import socket

s = socket.socket()
host = socket.gethostname()
port = 8082
s.bind(('',port))
s.listen(5)

while True:
    c, addr = s.accept()
    print 'Got Connection from', addr
    s.send('peter')
    c.close()

