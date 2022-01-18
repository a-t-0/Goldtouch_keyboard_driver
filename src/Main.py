# Manages calling functions to determine which wires match which keystroke.
import random
import os, shutil
import shutil

# Import from files
from src.helper import *


class Main:
    """ """

    def __init__(self):
        print("hello world")
        # self.blink_green_light_on_pico()

    def get_right_gpio_pin_nrs(self):
        # pin_nrs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        # pin_nrs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16,17,18,19]
        pin_nrs = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            22,
        ]
        return pin_nrs

    def get_list_of_gpio_connections_on_fpc(self):
        left_to_right_gold_bars_on_top = [
            22,
            20,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0,
            19,
            18,
            17,
            16,
        ]
        used = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 19]

        used_fpc_slots = []
        for fpc_slot_index in range(0, len(left_to_right_gold_bars_on_top)):
            if left_to_right_gold_bars_on_top[fpc_slot_index] in used:
                used_fpc_slots.append(fpc_slot_index)
        print(f"used_fpc_slots={used_fpc_slots}")
        print(f"nr_of_slots={len(used_fpc_slots)}")
        # used_fpc_slots=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        return used_fpc_slots

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

    def get_key_matrix(self, filepath):
        # importing the module
        import json

        # reading the data from the file
        with open(filepath) as f:
            data = f.read()

        print("Data type before reconstruction : ", type(data))

        # reconstructing the data as a dictionary
        js = json.loads(data)

        print("Data type after reconstruction : ", type(js))
        print(js)
        return js

    def get_list_of_used_connections(self, dictionary):
        lefts = []
        rights = []
        merged = []
        for value in dictionary.values():
            lefts.append(value[0])
            rights.append(value[1])
            merged.append(value[0])
            merged.append(value[1])

        lefts = sorted(list(dict.fromkeys(lefts)))
        rights = sorted(list(dict.fromkeys(rights)))
        merged = sorted(list(dict.fromkeys(merged)))
        print(f"lefts={lefts}")
        print(f"rights={rights}")
        print(f"merged={merged}")


if __name__ == "__main__":
    # initialize main class
    main = Main()
