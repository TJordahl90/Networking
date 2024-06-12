import socket
import threading

def sendMessage():
    while True:
        msg = input().encode('utf-8')
        sock.sendall(msg)

def waitForMessage():
    while True:
        print(sock.recv(1024))

sock = socket.socket()

port = 40674

sock.connect(("127.0.0.1", port))

thread = threading.Thread(target=waitForMessage)
thread.start()

sendMessage()