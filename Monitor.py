import socket

sk = socket.socket()
sk.connect(("67.216.199.87", 12000))
sk.sendall("M".encode("utf-8"))
print("Connetcion Established.")
while True:
    accept_data = sk.recv(1024)
    accept_data = bytes([x ^ 22 for x in accept_data])
    print(accept_data.decode("utf-8"))
sk = socket.close()


