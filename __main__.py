import os
import subproccess
import socket
import sys
import threading
import time
import pickle
def start_lsw():
    subproccess.open(["source","lsw.sh"])
if not os.path.exists("lsw.sh"):
    import lswgen
print("Starting Windows")
t = threading.Thread(name='LSWStart',target=start_lsw)
t.start()
print('Connecting to the LSW Server')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect(("127.0.0.1",9221))
    except Exception as e:
        print(f'Can\'t connect: {e}\nRetry in 5 seconds...')
        time.sleep(5)
    print('Connected!')
    break
print('Connected to server.')
print('Welcome to LSW')
while True:
    print('Windows Shell>')
    cmd = input()
    cmd = cmd.split(" ")
    cmd = pickle.dumps(cmd)
    s.send(cmd)

    
