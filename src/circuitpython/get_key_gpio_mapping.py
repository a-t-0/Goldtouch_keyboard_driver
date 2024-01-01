import time

from gpio_pin_nrs import create_emtpy_pin_connection_matrix_dictionary, get_pico_gpio_pin_nrs
from keys import get_left_keys, get_right_keys
from pico_probing import get_connected_pins_per_key
from user_interface import ask_user_to_press_pin, print_matrix # circuitpython only

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


def get_key_connection_dictionary(abs_output_dir,filename,keys):
    # Get the hardcoded connection settings.
    
    pin_nrs = get_pico_gpio_pin_nrs()
    
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
