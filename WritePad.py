import socket

sk = socket.socket()
sk.connect(("67.216.199.87", 12000))

print("Connetcion Established.")
sk.sendall("W".encode("utf-8"))
while True:
    send_data = input(">>")
    if send_data == "exit":
        break
    send_data = send_data.encode("utf-8")
    send_data = bytes([x ^ 22 for x in send_data])
    sk.sendall(send_data)

sk.close()


