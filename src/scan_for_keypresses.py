# Imports from Raspberry Pico


frequency = 50 #hz
cycle_runtime_ms = 1 # ms
if 1000/cycle_runtime_ms <frequency:
    raise Exception("The frequency cannot be obtained because a single run takes longer than the amount of seconds available.")

gpio_columns=[0,1,2,3,4,5,6,7]
gpio_left_rows=[8,9,10,11,12,13,14,15] 
gpio_right_rows=[16,
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

def scan_for_keys(gpio_columns,gpio_left_rows,gpio_right_rows):
    currently_pressed_keys_left=[]
    currently_pressed_keys_right=[]
    
    # Loop through the rows, and send a signal per row.
    for gpio_column in gpio_columns:
        
        # Set a value/signal on that particular row.
        
        # Loop through the left hand columns
        for gpio_left_row in gpio_left_rows:
            if detect_connection_between_two_pins(gpio_left_row,gpio_column):
                currently_pressed_keys_left.append(gpio_left_row,gpio_column)
                
        # Loop through the right hand columns
        for gpio_right_row in gpio_right_rows:
            if detect_connection_between_two_pins(gpio_right_row,gpio_column):
                currently_pressed_keys_right.append(gpio_right_row,gpio_column)
                
    return currently_pressed_keys_left,currently_pressed_keys_right

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

def send_keys(previously_pressed_keys,currently_pressed_keys):
    for key in currently_pressed_keys:
        if not key in previously_pressed_keys:
            send_key_down(key)
    for key in previously_pressed_keys:
        if not key in currently_pressed_keys:
            send_key_up(key)
    return currently_pressed_keys
 
def send_key_down(key):
    print(f"pressing:{key}")

def send_key_up(key):
    print(f"releasing:{key}")