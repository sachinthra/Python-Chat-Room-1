import socket
import pickle

HEADERSIZE = 10
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while True :

    full_msg = b''
    new_msg = True
    while True : 
        msg = s.recv(10)
        if new_msg:
            #print(f"New message length : {msg[:HEADERSIZE ]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg
        if len(full_msg)-HEADERSIZE == msglen:
            #print("full msg rvd")
            #print(full_msg[HEADERSIZE:])
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(f"Sachinthra : {d['msg']} ")
            new_msg = True
            full_msg = b''
    print(full_msg)