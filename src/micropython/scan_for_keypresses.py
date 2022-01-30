# Imports from Raspberry Pico
from machine import Pin

# Import from Python library
import json

frequency = 50  # hz
cycle_runtime_ms = 1  # ms
if 1000 / cycle_runtime_ms < frequency:
    raise Exception(
        "The frequency cannot be obtained because a single run takes longer than the amount of seconds available."
    )

gpio_columns = [0, 1, 2, 3, 4, 5, 6, 7]
gpio_left_rows = [
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    26,
    27,
    28,
]
gpio_right_rows = [8, 9, 10, 11, 12, 13, 14, 15]

# Send signals to all 8 GPIO pins.
# Read out remaining 24 GPIO pins.

# If match is found, assume that key is pressed and hold.
# Loop through currently_pressed_keys:
# If new keypress is detected (w.r.t. incoming list of previously_pressed_keys):
# Send the key-press down action. (And hold that key).
# Append that key to a new list currently_pressed_keys.
# For key in previously_pressed_keys:
# if the key is not pressed anymore,
# If not key in currently_pressed_keys:
# send key up
# return currently_pressed_keys


def scan_for_keys(gpio_columns, gpio_left_rows, gpio_right_rows):
    currently_pressed_keys_left = []
    currently_pressed_keys_right = []

    # Loop through the rows, and send a signal per row.
    for gpio_column in gpio_columns:

        # Set a value/signal on that particular row.

        # Loop through the left hand columns
        for gpio_left_row in gpio_left_rows:
            if detect_connection_between_two_pins(gpio_left_row, gpio_column):
                currently_pressed_keys_left.append((gpio_left_row, gpio_column))

        # Loop through the right hand columns
        for gpio_right_row in gpio_right_rows:
            if detect_connection_between_two_pins(gpio_right_row, gpio_column):
                currently_pressed_keys_right.append((gpio_right_row, gpio_column))

    return currently_pressed_keys_left, currently_pressed_keys_right


def detect_connection_between_two_pins(left, right):

    # Set the output pin to GPIO pin nr 0.
    output_line = Pin(left, Pin.OUT)

    # Set the input pin to GPIO pin nr 1.
    input_line = Pin(right, Pin.IN, Pin.PULL_DOWN)

    # Put voltage/value of 1 [-] on GPIO pin 0.
    output_line.value(1)

    # Check if the input has an incoming value.
    # for i in range(0,10):
    #    time.sleep(0.01)
    if input_line.value():
        output_line.value(0)
        return True
    # print(f"{left},{right}")
    output_line.value(0)
    return False


def send_keys(dictionary, previously_pressed_keys, currently_pressed_keys):
    for key in currently_pressed_keys:
        if not key in previously_pressed_keys:
            send_key_down(dictionary, key)
    for key in previously_pressed_keys:
        if not key in currently_pressed_keys:
            send_key_up(dictionary, key)
    return currently_pressed_keys


def send_key_down(dictionary, button):
    print(f"pressing:{button}")
    for key, value in dictionary.items():
        # print(f'key={key}')
        print(f"value={value},button={button}")
        if value == button:
            print(f"item={key}")


def send_key_up(dictionary, key):
    print(f"releasing:{key}")
    # TODO: copy code of key down.


def read_dictionary_from_file(abs_output_dir, filename):

    # reading the data from the file
    with open(f"{abs_output_dir}/{filename}") as f:
        data = f.read()

    print("Data type before reconstruction : ", type(data))

    # reconstructing the data as a dictionary
    js = json.loads(data)

    print("Data type after reconstruction : ", type(js))
    print(js)


def get_left_dictionary():
    left_dictionary = {
        "F5": (16, 3),
        "F4": (16, 2),
        "C": (16, 4),
        "B": (16, 6),
        "PageDown": (None, None),
        "T": (16, 7),
        "Alt": (16, 4),
        "W": (None, None),
        "Q": (16, 3),
        "V": (16, 4),
        "S": (16, 6),
        "R": (16, 3),
        "Ctrl (Left)": (16, 5),
        "Ctrl (Right)": (16, 5),
        "Space Left": (None, None),
        "Home": (None, None),
        "Start": (16, 6),
        "X": (16, 4),
        "Space Right": (None, None),
        "Shift (Left)": (None, None),
        "`": (16, 2),
        "Z": (16, 4),
        "Esc": (16, 6),
        "Space Middle": (None, None),
        "4": (None, None),
        "PageUp": (None, None),
        "1": (None, None),
        "Tab (Right)": (None, None),
        "3": (None, None),
        "2": (None, None),
        "5": (16, 2),
        "6": (None, None),
        "Tab (Left)": (None, None),
        "Shift (Right)": (None, None),
        "End": (16, 3),
        "Fn": (None, None),
        "E": (16, 3),
        "D": (16, 5),
        "G": (16, 2),
        "F": (16, 5),
        "Caps Lock(Right)": (16, 3),
        "A": (16, 5),
        "Caps Lock(Left)": (16, 3),
        "F3": (None, None),
        "F2": (16, 2),
        "F1": (16, 2),
        "F7": (16, 3),
        "F6": (16, 2),
    }
    return left_dictionary


def get_right_dictionary():
    right_dictionary = {
        "F5": (16, 3),
        "F4": (16, 2),
        "C": (16, 4),
        "B": (16, 6),
        "PageDown": (None, None),
        "T": (16, 7),
        "Alt": (16, 4),
        "W": (None, None),
        "Q": (16, 3),
        "V": (16, 4),
        "S": (16, 6),
        "R": (16, 3),
        "Ctrl (Left)": (16, 5),
        "Ctrl (Right)": (16, 5),
        "Space Left": (None, None),
        "Home": (None, None),
        "Start": (16, 6),
        "X": (16, 4),
        "Space Right": (None, None),
        "Shift (Left)": (None, None),
        "`": (16, 2),
        "Z": (16, 4),
        "Esc": (16, 6),
        "Space Middle": (None, None),
        "4": (None, None),
        "PageUp": (None, None),
        "1": (None, None),
        "Tab (Right)": (None, None),
        "3": (None, None),
        "2": (None, None),
        "5": (16, 2),
        "6": (None, None),
        "Tab (Left)": (None, None),
        "Shift (Right)": (None, None),
        "End": (16, 3),
        "Fn": (None, None),
        "E": (16, 3),
        "D": (16, 5),
        "G": (16, 2),
        "F": (16, 5),
        "Caps Lock(Right)": (16, 3),
        "A": (16, 5),
        "Caps Lock(Left)": (16, 3),
        "F3": (None, None),
        "F2": (16, 2),
        "F1": (16, 2),
        "F7": (16, 3),
        "F6": (16, 2),
    }
    return right_dictionary


abs_output_dir = "/home/name/git/keyboard/Goldtouch_keyboard_driver/output"
abs_output_dir = ""
# read_left_dictionary(abs_output_dir,"manual_right_dictionary.txt")
left_dictionary = get_left_dictionary()
right_dictionary = get_right_dictionary()
# print(f"left_dictionary={left_dictionary}")
# print(f"right_dictionary={right_dictionary}")

currently_pressed_keys_left, currently_pressed_keys_right = scan_for_keys(
    gpio_columns, gpio_left_rows, gpio_right_rows
)
print(f"currently_pressed_keys_left={currently_pressed_keys_left}")
print(f"currently_pressed_keys_right={currently_pressed_keys_right}")

print(f"Doing left")
send_keys(left_dictionary, [], currently_pressed_keys_left)
print(f"Doing right")
send_keys(left_dictionary, [], currently_pressed_keys_right)
# send_keys(right_dictionary, [], currently_pressed_keys_right)
