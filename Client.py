import socket
max_char_len = 1024

s = socket.socket()
host = socket.gethostname()
port = 8081

s.connect(('71.9.176.217',port))
print s.recv(max_char_len)
s.close
