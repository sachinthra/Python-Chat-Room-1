import socket
import pickle
import time

d =  {'time': '','msg': ''}
HEADERSIZE = 10
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
print("Waiting to connect....")
clientsocket , address = s.accept()
print(f"connection from {address} has been establish!")

while True :
    
    d['msg']=input("Enter : ")
    #if d['msg']=='/exit' :

    named_tuple = time.localtime() # get struct_time
    d['time'] = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    msg = pickle.dumps(d)
    #msg = "welcome to the server!"
    msg = bytes(f'{len(msg):< {HEADERSIZE}}',"utf-8") + msg
   
    clientsocket.send(msg)
      

