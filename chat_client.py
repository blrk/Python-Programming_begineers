from socket import *

client = socket()
client.connect(('localhost', 12301))

while True:
    recData = client.recv(1024).decode()
    print("Server:", recData)
    data = input("Client:")
    client.send(bytes(data, 'utf-8'))
    if data == "bye":
        client.close()
        break