# Imports from Raspberry Pico
from machine import Pin, Timer
import time

led = Pin(25, Pin.OUT)

count = 0
while  count < 10:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
    count=count+1