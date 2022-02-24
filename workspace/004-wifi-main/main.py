#main.py
#runs after boot.py

import network

ACTIVATE_STA = False #Toggle here to activate/deactivate

sta_if = network.WLAN(network.STA_IF)

sta_if.active(ACTIVATE_STA)

if ACTIVATE_STA: 
  try:
    sta_if.connect('AP J6', 'mcu-8266')
    if sta_if.isconnected(): 
      print('INFO: connected to AP')
  except:
    print("Error: cannot connnect to AP")
  finally:
    gc.collect()




