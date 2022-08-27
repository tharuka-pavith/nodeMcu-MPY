import socket

server_sc = socket.socket()
server_sc.bind( ('', 7788) )
print('server running')
server_sc.listen(5)

conn, addr = server_sc.accept()

print('Client connected ', addr)


while True:
  msg = conn.recv(1024).decode('ascii')
  print('-> ', msg)
  
  if msg == '/exit': break
  

 
server_sc.close()


