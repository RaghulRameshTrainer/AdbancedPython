import socket

s=socket.socket()
print("Socket object created successfully")

port=12345

s.bind(('',port))
s.listen(5)

while True:
    c,addr=s.accept()
    print("Received the connection from:",addr)
    c.send("Response To Client".encode("UTF-8"))
    c.close()