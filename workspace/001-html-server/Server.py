import network
import os
import sys
from blinkLed import blink

try:
  import usocket as socket
except:
  import socket

sta = network.WLAN(network.STA_IF) #station mode

if not sta.isconnected():
  print("Device not connected to network!")
  blink(2,100,500, 3)
  sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind( ("localhost", 80) )
sock.listen(5)
conn, addr = sock.accept()
print('Connected with ', addr)
while True:
      
  request = str(conn.recv(1024))
  print("Request: ", request)
  response = '<html><head><title>Hello</title></head><body><h1>Welcome!</h1></body></html>'
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
    






