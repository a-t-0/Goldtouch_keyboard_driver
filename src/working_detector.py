from machine import Pin
import time

led = Pin(15, Pin.OUT)
output_line= Pin(0, Pin.OUT)
input_line = Pin(1, Pin.IN, Pin.PULL_DOWN)


while True:
    time.sleep(2)
    if(input_line.value()):
        led.toggle()
        time.sleep(0.5)
        print("connected")
    output_line.value(1)
    print("set high")