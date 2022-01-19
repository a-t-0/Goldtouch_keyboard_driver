from machine import Pin
import time


def get_right_keys():

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

    rows.append(row_0)
    rows.append(row_1)
    rows.append(row_2)
    rows.append(row_3)
    rows.append(row_4)
    rows.append(row_5)

    return rows


def get_left_keys():

    # Start at top left. Go Western reading, first left to right, then top to bottom
    rows = []
    row_0 = [
        "Esc",
        "F1",
        "F2",
        "F3",
        "F4",
        "F5",
        "F6",
        "F7",
    ]

    row_1 = [
        "Home",
        "`",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
    ]

    row_2 = [
        "PageUp",
        "Tab (Left)",
        "Tab (Right)",
        "Q",
        "W",
        "E",
        "R",
        "T",
        "",
    ]

    row_3 = [
        "PageDown",
        "Caps Lock(Left)",
        "Caps Lock(Right)",
        "A",
        "S",
        "D",
        "F",
        "G",
    ]

    row_4 = [
        "End",
        "Shift (Left)",
        "Shift (Right)",
        "Z",
        "X",
        "C",
        "V",
        "B",
    ]

    row_5 = [
        "Fn",
        "Ctrl (Left)",
        "Ctrl (Right)",
        "Start",
        "Alt",
        "Space Left",
        "Space Middle",
        "Space Right",
    ]
    rows.append(row_0)
    rows.append(row_1)
    rows.append(row_2)
    rows.append(row_3)
    rows.append(row_4)
    rows.append(row_5)

    return rows


def get_right_gpio_pin_nrs():
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
        21,
        22,
        26,
        27,
        28,
    ]
    return pin_nrs


def create_emtpy_pin_connection_matrix_dictionary(rows):
    connected_pins_per_key = {}
    for row in rows:
        for key in row:
            connected_pins_per_key[key] = None
    return connected_pins_per_key


def store_pin_connection_pairs_per_key(rows, pin_nrs):
    connected_pins_per_key = create_emtpy_pin_connection_matrix_dictionary(rows)
    for row in rows:
        for key in row:
            ask_user_to_press_pin(key)
            left, right = get_connected_pins_per_key(pin_nrs)
            connected_pins_per_key[key] = (left, right)
            if not left is None and not right is None:
                print(f"Done, got for key:{key} left={left},right={right}")
            else:
                print(f"Failed for key:{key} left={left},right={right}")
    print(connected_pins_per_key)
    return connected_pins_per_key


def ask_user_to_press_pin(key):
    val = input(f"Please press and hold: {key} untill we say:done.")
    print(val)


def get_connected_pins_per_key(pin_nrs):
    for left in pin_nrs:
        for right in pin_nrs:
            if left != right:
                # print(f'test left={left},right={right}')
                has_connection = detect_connection_between_two_pins(left, right)
                # print(f"has_connection={has_connection}")
                if has_connection:
                    return left, right
    return None, None


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
        return True
    # print(f"{left},{right}")
    return False


def export_connected_pins_per_key(abs_output_dir, filename, connected_pins_per_key):
    write_dictionary_to_file(f"{abs_output_dir}/{filename}", connected_pins_per_key)
    lines = []
    for key, value in connected_pins_per_key.items():
        lines.append("%s:%s\n" % (key, value))
    write_to_file(f"{abs_output_dir}/{filename}", lines)


def write_dictionary_to_file(abs_filepath, dictionary):
    import json

    with open(abs_filepath, "w") as convert_file:
        convert_file.write(json.dumps(dictionary))


def write_to_file(abs_filepath, lines):
    f = open(abs_filepath, "w")
    for line in lines:
        f.write(line)
    f.close()


# print(detect_connection_between_two_pins(16, 17))
abs_output_dir = "/home/name/git/keyboard/Goldtouch_keyboard_driver/output"
abs_output_dir = ""
# sample_dictionary = {"Name": "Bob", "Age": 28}

# Get the hardcoded connection settings.
right_rows = get_right_keys()
left_rows = get_left_keys()
pin_nrs = get_right_gpio_pin_nrs()

# Ask user to press keys to get the keyboard wirign connection matrix
connected_pins_per_key_left = store_pin_connection_pairs_per_key(left_rows, pin_nrs)
# Export the keyboard wiring matrix
export_connected_pins_per_key(
    abs_output_dir, "left_dictionary.txt", connected_pins_per_key_left
)
connected_pins_per_key_right = store_pin_connection_pairs_per_key(right_rows, pin_nrs)


export_connected_pins_per_key(
    abs_output_dir, "right_dictionary.txt", connected_pins_per_key_right
)
