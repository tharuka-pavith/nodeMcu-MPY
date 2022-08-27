import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client_sock.connect( ('localhost', 8899) )

client_sock.connect( ('192.168.43.63', 7788) ) #micropython

####
print('Enter your messages to send (enter "/exit" to exit chat) ')

while True:
    msg = input('-> ')
    
    client_sock.send(msg.encode('ascii'))
    
    if msg == '/exit':
        break

client_sock.close()