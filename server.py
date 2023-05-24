import socket 
s = socket.socket()
print('Socket uspesno napravljen')
port = 55989
s.bind(('127.0.0.1', port))
print(f' socket bind to port')
s.listen(5)
print('Socket is listening')
while True:
    c, addr = s.accept()
    print(f'Socket prijavi vezu sa kljucem {addr}')
    message = ('Hvala za tvoju konekciju')
    c.send(message.encode())
    c.close()