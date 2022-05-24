from socket import *
from time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 12301))
server.listen()
conn, addr = server.accept()

while True:
    data = input('Server:')
    if data == "bye":
        conn.close()
        break
    conn.send(bytes(data, 'utf-8'))
    recData = conn.recv(1024).decode()
    print("Client:", recData)
    