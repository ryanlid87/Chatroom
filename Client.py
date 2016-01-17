import socket
max_char_len = 1024

s = socket.socket()
host = socket.gethostname()
port = 8080

s.connect((host,port))
print s.recv(max_char_len)
s.close
