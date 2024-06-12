import socket
import threading

def sendMessage():
    while True:
        msg = input().encode('utf-8')
        client.sendall(msg)

def waitForMessage():
    while True:
        print(client.recv(1024))

# Sets up a socket binding it on a port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 40674
sock.bind(("", port))
sock.listen(0)


client, addr = sock.accept()

print("Connected to", addr)

thread = threading.Thread(target=waitForMessage)
thread.start()

sendMessage()

client.close()