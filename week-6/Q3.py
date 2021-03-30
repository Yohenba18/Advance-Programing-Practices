#server
import socket

def server_651():

host = socket.gethostname()
port = 5000

server_socket = socket.socket()

server_socket.bind((host, port))

server_socket.listen(2)
conn, address = server_socket.accept()
print("Connection from: " + str(address))
while True:

data651 = conn.recv(1024).decode()
if not data651:

break
print("from client: " + str(data651))
data651 = input(' Enter pong message: ')
conn.send(data651.encode())

conn.close()

if __name__ == '__main__':
server_651()

#client
import socket

def client_651():
host = socket.gethostname()

port = 5000

client_socket = socket.socket()
client_socket.connect((host, port))

message651 = input(" Enter ping message: ")

while message651.lower().strip() != 'stop':
client_socket.send(message651.encode())
data = client_socket.recv(1024).decode()

print('From server: ' + data)

message651 = input(" Enter ping message ")

client_socket.close()

if __name__ == '__main__':
client_651()