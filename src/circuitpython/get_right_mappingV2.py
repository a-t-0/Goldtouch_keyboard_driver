import time

import board # circuitpython only
import digitalio # circuitpython only

def get_right_keys():

    # Start at top left. Go Western reading, first left to right, then top to bottom
    rows = []
    row_0 = [
        "F8",
        "F9",
        "F10",
        "F11",
        "F12",
        "SCROLL_LOCK",
        "INSERT",
        "DELETE",
    ]
    row_1 = [
        "7",
        "8",
        "9",
        "0",
        "MINUS",
        "EQUAL",
        "BACKSPACE",
        "BSPC",
    ]
    row_2 = [
        "Y",
        "U",
        "I",
        "O",
        "P",
        "LBRACKET",
        "RBRACKET",
        "BACKSLASH",
    ]
    row_3 = [
        "H",
        "J",
        "K",
        "L",
        "SEMICOLON",
        "QUOTE",
        "ENTER",
        "ENT",
    ]
    row_4 = [
        "N",
        "m",
        "COMMA",
        "DOT",
        "SLASH",
        "RIGHT_SHIFT",
        "UP",
        "PRINT_SCREEN",
    ]
    row_5 = [
        "SPACE",
        "SPC",
        "RIGHT_ALT",
        "RIGHT_SUPER",
        "RIGHT_CONTROL",
        "LEFT",
        "DOWN",
        "RIGHT",
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
        "ESCAPE",
        "F1",
        "F2",
        "F3",
        "F4",
        "F5",
        "F6",
        "F7",
    ]
    row_1 = [
        "HOME",
        "GRAVE",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
    ]
    row_2 = [
        "PGUP",
        "TAB",
        "TAB",
        "Q",
        "W",
        "E",
        "R",
        "T",
    ]
    row_3 = [
        "PGDOWN",
        "CAPS_LOCK",
        "CAPSLOCK",
        "A",
        "S",
        "D",
        "F",
        "G",
    ]
    row_4 = [
        "END",
        "LEFT_SHIFT",
        "LSHIFT",
        "Z",
        "X",
        "C",
        "V",
        "B",
    ]
    row_5 = [
        "ASTERISK",
        "LEFT_CONTROL",
        "LCTRL",
        "LEFT_SUPER",
        "LEFT_ALT",
        "SPACE",
        "SPC",
        "SPACE",
    ]

    rows.append(row_0)
    rows.append(row_1)
    rows.append(row_2)
    rows.append(row_3)
    rows.append(row_4)
    rows.append(row_5)

    return rows

def get_rows():
    # pin_nrs = [0, 1, 2, 3, 4, 5, 6, 7]
    pin_nrs = [0, 1, 2, 3, 4, 5, 6, 7,8,9, 10, 11, 12, 13, 14, 15,16,17,18,19,20,21,22,26,27,28]
    return pin_nrs

def get_columns():
    # pin_nrs = [8,9, 10, 11, 12, 13, 14, 15,16,17,18,19,20,21,22,26,27,28]
    pin_nrs = [0, 1, 2, 3, 4, 5, 6, 7,8,9, 10, 11, 12, 13, 14, 15,16,17,18,19,20,21,22,26,27,28]
    return pin_nrs

def get_right_gpio_pin_nrs():
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

def get_index_of_pin_nr(pin_nr):
    # TODO: this mapping can be created once instead of for every key.
    pin_nrs=get_right_gpio_pin_nrs()
    for i in range(len(pin_nrs)):
        if pin_nrs[i] == pin_nr:
            return i

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
    print('matrix')
    print_matrix(connected_pins_per_key, rows)
    return connected_pins_per_key

def print_matrix(connected_pins_per_key, rows):
    for row in rows:
        new_line = ""
        for key in row:
            new_line=f'{new_line}  {key}: {connected_pins_per_key[key]}'
            # print(f'{key}: {connected_pins_per_key[key]}')
        print(new_line)
        # print("")
    return connected_pins_per_key


def ask_user_to_press_pin(key):
    val = input(f"On the keyboard that you are testing: press and hold: {key}, Press <enter> with your normal keyboard in this terminal to start scanning>, hold: {key} untill we say: done .")
    print(val)


def get_connected_pins_per_key(pin_nrs):
    for left in get_rows():
        for right in get_columns():
            if left != right:
                print(f'check: left={left},right={right}')
                #has_connection = detect_connection_between_two_pins(left, right)
                has_connection= detect_connection_between_two_pins_circuitpythonV5(left, right)
                
                # print(f"has_connection={has_connection}")
                if has_connection:
                    return left, right
    return None, None


def detect_connection_between_two_pins_micropython(left, right):
    # Import for micropython
    from machine import Pin
    
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

def detect_connection_between_two_pins_circuitpythonV5(left, right):
    out = digitalio.DigitalInOut(pin_to_board_pin(left))
    out.direction = digitalio.Direction.OUTPUT
    out.value=1
    
    input = digitalio.DigitalInOut(pin_to_board_pin(right))
    input.direction = digitalio.Direction.INPUT
    input.pull = digitalio.Pull.DOWN

    # Check if the input has an incoming value.
    if input.value:
        out.deinit()
        input.deinit()
        return True
    #row.value = 0
    out.deinit()
    input.deinit()
    return False
    
def pin_to_board_pin(pin_nr):
    if pin_nr==0:
        return board.GP0
    elif pin_nr==1:
        return board.GP1
    elif pin_nr==2:
        return board.GP2
    elif pin_nr==3:
        return board.GP3
    elif pin_nr==4:
        return board.GP4
    elif pin_nr==5:
        return board.GP5
    elif pin_nr==6:
        return board.GP6
    elif pin_nr==7:
        return board.GP7
    elif pin_nr==8:
        return board.GP8
    elif pin_nr==9:
        return board.GP9
    elif pin_nr==10:
        return board.GP10
    elif pin_nr==11:
        return board.GP11
    elif pin_nr==12:
        return board.GP12
    elif pin_nr==13:
        return board.GP13
    elif pin_nr==14:
        return board.GP14
    elif pin_nr==15:
        return board.GP15
    elif pin_nr==16:
        return board.GP16
    elif pin_nr==17:
        return board.GP17
    elif pin_nr==18:
        return board.GP18
    elif pin_nr==19:
        return board.GP19
    elif pin_nr==20:
        return board.GP20
    elif pin_nr==21:
        return board.GP21
    elif pin_nr==22:
        return board.GP22
    elif pin_nr==23:
        return board.GP23
    elif pin_nr==24:
        return board.GP24
    elif pin_nr==25:
        return board.GP25
    elif pin_nr==26:
        return board.GP26
    elif pin_nr==27:
        return board.GP27
    elif pin_nr==28:
        return board.GP28
    else:
        raise Exception(f"No  pin found for: pin_nr={pin_nr}.")
    

def export_connected_pins_per_key(abs_output_dir,filename,connected_pins_per_key):
    filepath=f"{abs_output_dir}/{filename}"
    print(f'filepath={filepath}')
    write_dictionary_to_file(f"{abs_output_dir}/{filename}", connected_pins_per_key)
    #lines = []
    #for key, value in connected_pins_per_key.items():
    #    lines.append("%s:%s\n" % (key, value))
    #write_to_file(f"{abs_output_dir}/lines.txt", lines)


def write_dictionary_to_file(abs_filepath, dictionary):
    import json

    with open(abs_filepath, "w") as convert_file:
        convert_file.write(json.dumps(dictionary))


def write_to_file(abs_filepath, lines):
    f = open(abs_filepath, "w")
    for line in lines:
        f.write(line)
    f.close()


def get_key_connection_dictionary(abs_output_dir,filename,keys):
    # Get the hardcoded connection settings.
    
    pin_nrs = get_right_gpio_pin_nrs()
    
    # Get the circuitpython pins:
    # Ask user to press keys to get the keyboard wirign connection matrix
    connected_pins_per_key = store_pin_connection_pairs_per_key(keys, pin_nrs)
    
    # Export the keyboard wiring matrix
    #export_connected_pins_per_key(abs_output_dir,filename, connected_pins_per_key)
    
    return connected_pins_per_key


# print(detect_connection_between_two_pins(16, 17))
abs_output_dir = "/home/name/git/Goldtouch_keyboard_driver/output"
abs_output_dir = ""
left_filename="left_dictionary.txt"
right_filename="right_dictionary.txt"
# sample_dictionary = {"Name": "Bob", "Age": 28}

right_keys = get_right_keys()
left_keys = get_left_keys()
left_dic=get_key_connection_dictionary(abs_output_dir,left_filename,right_keys)
right_dic= get_key_connection_dictionary(abs_output_dir,right_filename,left_keys)
