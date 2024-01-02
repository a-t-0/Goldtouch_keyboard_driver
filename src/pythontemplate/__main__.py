"""Entry point for the project."""


from src.pythontemplate.debugging import list_faulty_wires
from src.pythontemplate.get_key_gpio_mapping import (
    get_key_connection_dictionary,
)
from src.pythontemplate.keys import get_left_keys, get_right_keys
from src.pythontemplate.user_interface import (
    ask_user_to_get_left_or_right_half,
)

# Output configuration.
abs_output_dir = "/home/name/"
left_keyboard_gpio_dict_file = "left_keyboard_gpio_dict.py"
right_keyboard_gpio_dict_file = "right_keyboard_gpio_dict.py"

right_keys = get_right_keys()
left_keys = get_left_keys()


# This asks you to press the keys, then it scans all GPIO ports on the
# Raspberry Pico, and determines which two GPIO pins connect which key on the
# keyboard.
if ask_user_to_get_left_or_right_half("left"):
    left_dic = get_key_connection_dictionary(left_keys)
    list_faulty_wires(left_dic, True)
if ask_user_to_get_left_or_right_half("right"):
    right_dic = get_key_connection_dictionary(right_keys)
    list_faulty_wires(right_dic, False)

# TODO: create separate function/file that takes in the wiring and key-pin
# relations to tell the user which wire is not connected properly if a
# keyboard button does not work.
# TODO: rewrite get_mapping_V2 such that it also automatically outputs which
# wire is not connected properly, if there is any wire not connected
# properly.
