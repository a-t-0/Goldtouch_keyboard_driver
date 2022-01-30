from machine import Pin
import time

# Do disco if connection is detected
led = Pin(15, Pin.OUT)
# Set the output pin to GPIO pin nr 0.
output_line = Pin(0, Pin.OUT)
# Set the input pin to GPIO pin nr 1.
input_line = Pin(1, Pin.IN, Pin.PULL_DOWN)


while True:
    time.sleep(2)

    # Check if the input pin nr 1 has an incoming value.
    if input_line.value():

        # Connection is found, start disco!
        led.toggle()
        # Not quite time yet, let's hang back.
        time.sleep(0.5)
        # Celebrate victory.
        print("connected")

    # Put voltage/value of 1 [-] on GPIO pin 0.
    output_line.value(1)
    print("Started sending output signal on output pin nr 0.")
