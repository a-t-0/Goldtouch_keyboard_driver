"""Entry point for the project."""

from src.pythontemplate.debugging import get_rows_and_cols, list_faulty_wires
from src.pythontemplate.generate_kmk_main import generate_kmk_main
from src.pythontemplate.get_key_gpio_mapping import (
    get_key_connection_dictionary,
)
from src.pythontemplate.hardcoded_wiring import hardcoded_lhs, hardcoded_rhs
from src.pythontemplate.keys import get_left_keys, get_right_keys
from src.pythontemplate.user_interface import (
    ask_user_to_get_left_or_right_half,
    print_messages,
)

# Output configuration.
abs_output_dir = "/home/name/"
left_keyboard_gpio_dict_file = "left_keyboard_gpio_dict.py"
right_keyboard_gpio_dict_file = "right_keyboard_gpio_dict.py"


right_keys = get_right_keys()
left_keys = get_left_keys()

get_rows_and_cols(hardcoded_lhs, is_left=True)
get_rows_and_cols(hardcoded_rhs, is_left=False)

# This asks you to press the keys, then it scans all GPIO ports on the
# Raspberry Pico, and determines which two GPIO pins connect which key on the
# keyboard.
if ask_user_to_get_left_or_right_half("left"):
    left_dic = get_key_connection_dictionary(left_keys)
    print_messages(messages=list_faulty_wires(left_dic, True))
if ask_user_to_get_left_or_right_half("right"):
    right_dic = get_key_connection_dictionary(right_keys)
    print_messages(messages=list_faulty_wires(right_dic, False))

# If this code is not ran on the Pico, generate the Python code that creates
# the KMK main.py file/driver for the keyboard.
generate_kmk_main()
