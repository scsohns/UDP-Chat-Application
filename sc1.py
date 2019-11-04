from socket import*
import time
import threading
from random import randint
import sys

def Server():
    print("Chat Commands:\n\tquit() to exit\n\thist() to view chat history\n\tfile() to transfer a file\n")
    host = gethostbyname(gethostname())
    print("IP:",host)
    print()
    port = 6000

    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((host,port))
    print("Server: Chat room created")
    hist = []
    username = "p1"
    data, addr = s.recvfrom(1024)
    message = data.decode('utf-8')
    print(message)
    s.sendto("Server: Successfully connected to chat.".encode('utf-8'), addr)

    threading.Thread(target=recv, args=(s,hist)).start()
    send(s, addr, hist, username)

    s.close()
    return

def Client(IP, port):
    print("Chat Commands:\n\tquit() to exit\n\thist() to view chat history\n\tfile() to transfer a file\n")
    host = gethostbyname(gethostname())
    try:
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((host,port))
    except Exception:
        print("Please try again")
        quit()

    server = (IP, 6000)
    hist = []
    username = "p2"
    s.sendto(("Server: "+username+" has joined the chat.").encode('utf-8'), server)

    data, addr = s.recvfrom(1024)
    message = data.decode('utf-8')
    print(message)

    threading.Thread(target=recv, args=(s,hist)).start()
    send(s, server, hist, username)
    return

def send(s, dest, hist, username):
    while True:
        message = input()
        if message == "hist()":
            print()
            print("Chat History")
            print("__________________________________")
            for i in hist:
                print(i)
            print("__________________________________")

        elif message == "quit()":
            try:
                s.sendto("User has quit. Type quit() to exit".encode('utf-8'), dest)
                time.sleep(5)
            except Exception:
                pass
            s.close()
            break
        elif message == "file()":
            filename = input("Please enter the file name:\n")
            ext = filename[filename.rindex('.'):]
            file = open(filename, 'rb')
            file_data = file.read(2048)
            servermessage = ">>File"+ext
            s.sendto(servermessage.encode('utf-8'), dest)
            s.sendto(file_data, dest)
        elif message == " ":
            pass
        else:
            message = username +":\t" + message
            s.sendto(message.encode('utf-8'), dest)
            hist.append(message)


def recv(s, hist):
    while True:
        data, addr = s.recvfrom(1024)
        message = data.decode('utf-8')
        if message[0:6] == ">>File":
            ext = message[6:10]
            data, addr = s.recvfrom(2048)
            filename = input('Server: File received. Please enter a file name.(no extension)\n')
            file = open(filename+ext, 'wb')
            file.write(data)
            file.close()
        else:
            print(message)
            hist.append(message)


i = int(input("Enter 0 if server, Enter 1 if client:"))
if i == 0:
    Server()
elif i ==1:
    #Client("192.168.56.1", randint(6000,8000))
    Client(input("Please enter IP: "), int(input("Please enter a port number between 6001 and 10000: ")))
else:
    print("Invalid")
print("Connection Terminated")
sys.exit()
