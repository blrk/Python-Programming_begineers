from socket import *

client = socket()
client.connect(('localhost', 12300))
print("client connected to the server")

data = client.recv(1024).decode()
print("data received from the server:", data)
