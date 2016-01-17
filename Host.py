import socket

s = socket.socket()
host = socket.gethostname()
port = 8082
s.bind(('',port))
s.listen(5)
data = 'Welcome to the chat'

while True:
    c, addr = s.accept()
    print 'Got Connection from', addr
    c.send(data)
    while data != 'q' or data != 'Q':
        data = c.recv(1024)
        print data
        c.send(data)
    c.close()

