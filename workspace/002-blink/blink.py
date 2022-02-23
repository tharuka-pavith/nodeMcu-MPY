from machine import Pin, Signal
import time, gc

def blink(pin: int=2, t_on: int=100, t_off: int=1000, count: int=10) -> None:
  # Use this function to make a blinking signal i.e. To blink an LED
  
  led = Pin(pin, Pin.OUT)
  
  l = Signal(led, invert=True) #Making a level of abstraction
  
  for i in range(10):
    l.on()
    print('Led on')
    time.sleep_ms(t_on)
    
    l.off()
    print('Led off')
    time.sleep_ms(t_off)
  
  gc.collect()
  

if __name__ == '__main__':
  blink()
  

