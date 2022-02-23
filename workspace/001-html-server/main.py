from machine import I2C, Pin

scl = Pin(5)
sda = Pin(4)


i2c = I2C(scl= scl, sda = sda, freq=100_000)
addr = i2c.scan()[0]

print(hex(addr))

i2c.writeto(addr, chr(23))






