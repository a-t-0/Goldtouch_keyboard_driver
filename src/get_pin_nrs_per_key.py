from machine import Pin
import time


def get_right_keys():
    keys = []

    # Start at top left. Go Western reading, first left to right, then top to bottom
    rows = []
    row_0 = [
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "ScrlLk",
        "Insert",
        "Delete",
    ]
    row_1 = [
        "7",
        "8",
        "9",
        "10",
        "-",
        "=",
        "Backspace (left half)",
        "Backspace (right half)",
    ]
    row_2 = [
        "y",
        "u",
        "i",
        "o",
        "p",
        "[",
        "]",
        "\\",
    ]
    row_3 = [
        "h",
        "j",
        "k",
        "l",
        ";",
        "'",
        "Enter (left half)",
        "Enter (right half)",
    ]
    row_4 = [
        "n",
        "m",
        ",",
        ".",
        "/",
        "Shift",
        "Up arrow",
        "Print Scrn",
    ]
    row_5 = [
        "Spacebar (left half of right bar)",
        "Spacebar (right half of right bar)",
        "alt",
        "Start",
        "Ctrl",
        "Left arrow",
        "Down Arrow",
        "Right Arrow",
    ]

    rows.append(
        row_0, row_1, row_2, row_3, row_4, row_5,
    )
    return rows


def get_right_gpio_pin_nrs():
    pin_nrs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    return pin_nrs


def create_emtpy_pin_connection_matrix_dictionary(rows):
    connected_pins_per_key = {}
    for row in rows:
        for key in row:
            connected_pins_per_key[key] = None
    return connected_pins_per_key


def get_connected_pins_per_key(pin_nrs):
    for left in pin_nrs:
        for right in pin_nrs:
            if left != right:
                if detect_connection_between_two_pins(left, right):
                    return left, right
    return None


def detect_connection_between_two_pins(left, right):

    # Set the output pin to GPIO pin nr 0.
    output_line = Pin(left, Pin.OUT)

    # Set the input pin to GPIO pin nr 1.
    input_line = Pin(right, Pin.IN, Pin.PULL_DOWN)

    # Put voltage/value of 1 [-] on GPIO pin 0.
    output_line.value(1)

    # Check if the input has an incoming value.
    if input_line.value():
        return True
    else:
        return False


def store_pin_connection_pairs_per_key(rows, pin_nrs):
    connected_pins_per_key = create_emtpy_pin_connection_matrix_dictionary(rows)
    for row in rows:
        for key in row:
            left, right = get_connected_pins_per_key(pin_nrs)


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
