# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect( ('data.pr4e.org', 80 ))

# Writing a simple browser in python
# ERROR: Named this file as scoket and import didnt work
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # \r is give return \n is for new line
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()


