import socket
import sys
ser = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host =  'Local Host'
port = 7070
ser.bind()
ser_add = ((host,port))
print('Trying to connect')
ser.connect(ser_add)