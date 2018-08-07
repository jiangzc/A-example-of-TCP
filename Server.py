import socketserver
import time

class MyServer(socketserver.BaseRequestHandler):
    monitors = []
    def handle(self):
        accept_data = self.request.recv(1024).decode("utf-8")
        addr = (self.client_address[0] + ": ").encode("utf-8")
        addr = bytes([x ^ 22 for x in addr])
        if accept_data == "M":
            if self.request not in self.monitors:
                self.monitors.append(self.request)
            while 1:
                time.sleep(1)  # to keep connection alive

        elif accept_data == "W":
            while 1:
                accept_data = self.request.recv(1024)
                print(accept_data)
                for conn in self.monitors:
                    conn.sendall(addr + accept_data)
