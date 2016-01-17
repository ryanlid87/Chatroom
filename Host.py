import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))

s.listen(5)

while True:
    c, addr = s.accept()
    print 'Got Connection from', addr
    c.send('thank you for connection')
    c.close()
