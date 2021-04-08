import socket, subproccess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    sock, addr = s.listen(1) 
    while True:
        if addr[0] != '127.0.0.1':
            # NEVER take connecttions from anyone but ourselves
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock, addr = s.listen(1) 
        break
    cmd = bytearray()
    data = b''
    while data != b'\r\n':
        data = s.recv(2)
        cmd += data
    print(cmd)



