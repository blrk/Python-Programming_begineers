from socket import *
from time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 12300))
server.listen()
print("Server ready and listening at port 12300")
connection, address = server.accept()
print("server connected to the client")
connection.send(bytes("hello from server"+ ctime(), 'utf-8'))
print("data sent to client")