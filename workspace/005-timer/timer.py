from machine import Timer, Pin
import time

class Led:
  def __init__(self, pin):
    self.led = Pin(pin, Pin.OUT)
    self.led.value(1)
   
  def blink(self,t):
    self.led.value(0)
    time.sleep_ms(100)
    self.led.value(1)
 

def start_timer():
 led = Led(2) #builtin LED is at pin 2
 tmr = Timer(-1)
 try:
   tmr.init(period=5000, mode=Timer.PERIODIC, callback=led.blink)
 except:
   raise
   
if __name__ == '__main__':
  start_timer()
 

  

  
  
  


