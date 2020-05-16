import socket
import select
import errno
import sys
import threading
import ctypes  
import easygui
from tkinter import *


HEADER_LENGTH = 10

my_username = easygui.enterbox("Enter your name : ")

IP = "127.0.0.1"
PORT = 1234


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((IP, PORT))


client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

root = Tk()
root.geometry("500x500")
lv = Variable()
lst = Listbox(root, listvariable=lv,height=25,width = 79 )
lst.place(x=10,y=10)
msg = ''
def add(event):
    "add item to listbox with entry when Return is pressed"
    global msg
    msg = entry.get()
    lst.insert(END, (str(b'%s > ' % (username),'utf-8').rjust(15) + msg))
    print(str(b'%s > ' % (username),'utf-8').rjust(10) + msg)
    
    v.set("")
v = StringVar()
Label(root, text=(username)).place(x=20,y=450)
entry = Entry(root, textvariable=v,width=55)
entry.place(x=100,y=450)
entry.bind("<Return>", add)
#btn = Button(root,text="exit",command=root.quit)
#btn.place(x=450,y=450)
def sendMsg():
    #t1 = Text(root, height=100, width=50)
    #t1.place(x=0,y=450)
    while True:
        global msg
        message = msg
        

    
        if message:

           
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)
            msg=''


def recvMsg():
    while True:
        try:
     
            while True:

              
                username_header = client_socket.recv(HEADER_LENGTH)

                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()

                
                username_length = int(username_header.decode('utf-8').strip())

               
                username = client_socket.recv(username_length).decode('utf-8')

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')

                # Print message
                print(f'{username.rjust(10)} > {message}')
                #lst.insert(END, (f'{username.rjust(10)} > {message}'))
                lst.insert(END, ((str(f'{username}').rjust(15) + " > "+ str(f'{message}'))))
        except IOError as e:
           
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            
            continue

        except Exception as e:
            
            print('Reading error: '.format(str(e)))
            sys.exit()

thread1 = threading.Thread(target = sendMsg)
thread1.start()
thread2 = threading.Thread(target = recvMsg)
thread2.start()
root.mainloop()
