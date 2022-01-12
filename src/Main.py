# Example code that creates plots directly in report
# Code is an implementation of a genetic algorithm
import random
from matplotlib import pyplot as plt
from matplotlib import lines
import matplotlib.pyplot as plt
import os, shutil
import numpy as np
import shutil

# Imports from Raspberry Pico
from machine import Pin, Timer


class Main:
    """ """

    def __init__(self):
        print("hello world")
        self.blink_green_light_on_pico()

    def blink_green_light_on_pico(self):
        led = Pin(25, Pin.OUT)
        LED_state = True
        tim = TIMER()
        tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)

    def tick(self, timer):
        global led, LED_state
        LED_state = not LED_state
        led.value(LED_state)

    def addTwo(self, x):
        """adds two to the incoming integer and returns the result of the computation.

        :param x:

        """
        return x + 2

    def delete_directory_contents(self, folder):
        """

        :param folder:

        """
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (file_path, e))


if __name__ == "__main__":
    # initialize main class
    main = Main()
