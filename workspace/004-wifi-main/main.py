#main.py
#runs after boot.py

import network

sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)

try:
  sta_if.connect('AP J6', 'tharuka.98')
except:
  print("Error: cannot connnect to AP")
finally:
  gc.collect()



