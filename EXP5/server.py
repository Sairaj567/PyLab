import socket
s = socket.socket()
print("Socket created")

s.bind(('192.168.11.70',6234))
s.listen(100)
print("Waiting for connection")

while True:
    c,addr=s.accept()
    name = c.recv(1024).decode()
    print("Connected with",addr,name)

c.close()