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

def get_rows():
    pin_nrs = [0, 1, 2, 3, 4, 5, 6, 7]
    return pin_nrs

def get_columns():
    pin_nrs = [9, 10, 11, 12, 13, 14, 15,16,17,18,19,20,21,22,26,27,28]
    return pin_nrs

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


def store_pin_connection_pairs_per_key(rows, pin_nrs,circuitpython_pins=None):
    connected_pins_per_key = create_emtpy_pin_connection_matrix_dictionary(rows)
    for row in rows:
        for key in row:
            ask_user_to_press_pin(key)
            left, right = get_connected_pins_per_key(pin_nrs,circuitpython_pins)
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


def get_connected_pins_per_key(pin_nrs,circuitpython_pins=None):
    for left in get_rows():
        for right in get_columns():
            if left != right:
                # print(f'test left={left},right={right}')
                #has_connection = detect_connection_between_two_pins(left, right)
                #has_connection = detect_connection_between_two_pins_circuitpythonV0(left, right,circuitpython_pins)
                #has_connection = detect_connection_between_two_pins_circuitpythonV1(left, right)
                #has_connection= detect_connection_between_two_pins_circuitpythonV2(left, right)
                #has_connection= detect_connection_between_two_pins_circuitpythonV4(left, right,None)
                has_connection= detect_connection_between_two_pins_circuitpythonV5(left, right,None)
                
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

def detect_connection_between_two_pins_circuitpythonV1(left, right):
    # Import for circuitpython.
    import board 
    import digitalio
    print(f'left={left},right={right}')
    
    left_pin=get_circuitpython_gpio_pin(board,left)
    right_pin=get_circuitpython_gpio_pin(board,right)
    # Set the output pin to GPIO pin nr 0.
    output_line = digitalio.DigitalInOut(left_pin)
    output_line.direction=digitalio.Direction.OUTPUT

    # Set the input pin to GPIO pin nr 1.
    input_line = digitalio.DigitalInOut(right_pin)
    input_line.direction=digitalio.Direction.INPUT

    # Put voltage/value of 1 [-] on GPIO pin 0.
    output_line.value = 1

    if input_line.value == 1:
        print(f'input_line.value={input_line.value}')
        output_line.value = 0
        print(f'input_line.value={input_line.value}')
        #output_line.direction=None
        #output_line=None
        #input_line.direction=None
        #input_line=None
        input_line.deinit()
        output_line.deinit()
        return True
    # print(f"{left},{right}")
    #output_line.direction=None
    #output_line=None
    #input_line.direction=None
    #input_line=None
    output_line.value = 0
    input_line.deinit()
    output_line.deinit()
    return False

def detect_connection_between_two_pins_circuitpythonV2(left, right):
    # Import for circuitpython.
    import board 
    import digitalio
    print(f'left={left},right={right}')
    
    left_pin=get_circuitpython_gpio_pin(board,left)
    right_pin=get_circuitpython_gpio_pin(board,right)
    print(f'right_pin={right_pin}')
    # Set the output pin to GPIO pin nr 0.
    output_line = digitalio.DigitalInOut(left_pin)
    output_line.direction=digitalio.Direction.OUTPUT
    if output_line.value == 1:
        raise Exception("The output line starts with value 1")

    # Set the input pin to GPIO pin nr 1.
    input_line = digitalio.DigitalInOut(right_pin)
    input_line.direction=digitalio.Direction.INPUT
    if input_line.value == 1:
        raise Exception("The input line starts with value 1")

    # Put voltage/value of 1 [-] on GPIO pin 0.
    output_line.value = 1

    if input_line.value == 1:
        print(f'input_line.value={input_line.value}')
        output_line.value = 0
        print(f'input_line.value={input_line.value}')
        #output_line.direction=None
        #output_line=None
        #input_line.direction=None
        #input_line=None
        input_line.deinit()
        output_line.deinit()
        return True
    # print(f"{left},{right}")
    #output_line.direction=None
    #output_line=None
    #input_line.direction=None
    #input_line=None
    output_line.value = 0
    input_line.deinit()
    output_line.deinit()
    return False

def detect_connection_between_two_pins_circuitpythonV0(left, right,circuitpython_pins):
    
    row_nr=get_index_of_pin_nr(left)
    col_nr=get_index_of_pin_nr(right)
    print(f'{left}row_nr={row_nr}, {right}col_nr={col_nr}')
    row=circuitpython_pins[row_nr]
    #print(f'row={row}')
    column=circuitpython_pins[col_nr]
    print(f'column={column}')
    
    row.value = 1

    # Check if the input has an incoming value.
    if column.value == 1:
        row.value = 0
        return True
    row.value = 0
    return False
    
def detect_connection_between_two_pins_circuitpythonV4(left, right,circuitpython_pins):
    print(f'left={left}')
    print(f'right={right}')
    left_boardpin=pin_to_board_pin(left)
    print(f'left_boardpin={left_boardpin}')
    print(f'left_boardpin type={type(left_boardpin)}')
    right_boardpin=pin_to_board_pin(right)
    out = digitalio.DigitalInOut(left_boardpin)
    out.direction = digitalio.Direction.OUTPUT
    out.value=1
    
    input = digitalio.DigitalInOut(right_boardpin)
    input.direction = digitalio.Direction.INPUT
    input.pull = digitalio.Pull.DOWN

    # Check if the input has an incoming value.
    if input.value:
        #row.value = 0
        return True
    #row.value = 0
    return False

def detect_connection_between_two_pins_circuitpythonV5(left, right,circuitpython_pins):
    print(f'left={left}')
    print(f'right={right}')
    left_boardpin=pin_to_board_pin(left)
    print(f'left_boardpin={left_boardpin}')
    print(f'left_boardpin type={type(left_boardpin)}')
    right_boardpin=pin_to_board_pin(right)
    out = digitalio.DigitalInOut(left_boardpin)
    out.direction = digitalio.Direction.OUTPUT
    out.value=1
    
    input = digitalio.DigitalInOut(right_boardpin)
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


def generate_circuitpython_gpio_pins(board):
    circuitpython_gpio_pins= [
        board.GP0,
        board.GP1,
        board.GP2, 
        board.GP3, 
        board.GP4, 
        board.GP5, 
        board.GP6, 
        board.GP7, 
        board.GP8, 
        board.GP9,
        board.GP10, 
        board.GP11, 
        board.GP12, 
        board.GP13,
        board.GP14, 
        board.GP15, 
        board.GP16, 
        board.GP17, 
        board.GP18, 
        board.GP19, 
        board.GP20, 
        board.GP21,
        board.GP22, 
        board.GP23, 
        board.GP24, 
        board.GP25, 
        board.GP26, 
        board.GP27, 
        board.GP28,
    ]
    return circuitpython_gpio_pins

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
    

def generate_rows_circuitpython(board,circuitpython_gpio_pins, digitalio):
    output_lines=[]
    for row in range(0,8):
        left_pin=get_circuitpython_gpio_pin(board,row)
        output_line = digitalio.DigitalInOut(left_pin)
        output_line.direction=digitalio.Direction.OUTPUT
        output_lines.append(output_line)
        #print(f'row={row}')
    return output_lines

def generate_columns_circuitpython(board,circuitpython_gpio_pins):
    input_lines=[]
    for column in range(8,28):
        right_pin=get_circuitpython_gpio_pin(board,column)
        input_line = digitalio.DigitalInOut(right_pin)
        input_line.direction=digitalio.Direction.INPUT
        input_lines.append(input_line)
        #print(f'column={column}')
    return input_lines

def get_circuitpython_gpio_pin(board,gpio_pin_nr):
    circuitpython_gpio_pins= [
        board.GP0,
        board.GP1,
        board.GP2, 
        board.GP3, 
        board.GP4, 
        board.GP5, 
        board.GP6, 
        board.GP7, 
        board.GP8, 
        board.GP9,
        board.GP10, 
        board.GP11, 
        board.GP12, 
        board.GP13,
        board.GP14, 
        board.GP15, 
        board.GP16, 
        board.GP17, 
        board.GP18, 
        board.GP19, 
        board.GP20, 
        board.GP21,
        board.GP22, 
        board.GP23, 
        board.GP24, 
        board.GP25, 
        board.GP26, 
        board.GP27, 
        board.GP28,
    ]
    return circuitpython_gpio_pins[gpio_pin_nr]


def export_connected_pins_per_key(abs_output_dir, connected_pins_per_key):
    write_dictionary_to_file(f"{abs_output_dir}/dictionary.txt", connected_pins_per_key)
    lines = []
    for key, value in connected_pins_per_key.items():
        lines.append("%s:%s\n" % (key, value))
    write_to_file(f"{abs_output_dir}/lines.txt", lines)


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
rows = get_right_keys()
pin_nrs = get_right_gpio_pin_nrs()

# Get the circuitpython pins:
circuitpython_pins=None
import board # circuitpython only
import digitalio # circuitpython only
##circuitpython_gpio_pins=generate_circuitpython_gpio_pins(board)
##circuitpython_pins=generate_rows_circuitpython(board,circuitpython_gpio_pins,digitalio)
##circuitpython_pins.extend(generate_columns_circuitpython(board,circuitpython_gpio_pins))


# Ask user to press keys to get the keyboard wirign connection matrix
connected_pins_per_key = store_pin_connection_pairs_per_key(rows, pin_nrs,circuitpython_pins)

# Export the keyboard wiring matrix
export_connected_pins_per_key(abs_output_dir, connected_pins_per_key)
