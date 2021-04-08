print("LSW Server Version 1.0")
import socket, subprocess, pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9221))
while True:
    s.listen(5)
    (sock, addr) = s.accept() 
    while True:
        cmd = bytearray()
        data = b''
        while data != b'\n':
            data = sock.recv(1)
            if data != b'\n':
                cmd += data
        response = subprocess.check_output(pickle.loads(bytes(cmd)))
        sock.send(bytes(response))
        sock.send(b'\xFF')



