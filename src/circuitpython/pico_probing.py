import digitalio
import board # circuitpython only

from gpio_pin_nrs import create_emtpy_pin_connection_matrix_dictionary, get_pico_gpio_pin_nrs
from keys import get_left_keys, get_right_keys
from user_interface import ask_user_to_press_pin, print_matrix # circuitpython only


def get_connected_pins_per_key(pin_nrs):
    for left in get_pico_gpio_pin_nrs():
        for right in get_pico_gpio_pin_nrs():
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
    
