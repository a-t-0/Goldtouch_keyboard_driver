"""Entry point for the project."""

from src.pythontemplate.get_key_gpio_mapping import (
    get_key_connection_dictionary,
)
from src.pythontemplate.keys import get_left_keys, get_right_keys

# TODO: cleanup make relative.
abs_output_dir = "/home/name/git/Goldtouch_keyboard_driver/output"
abs_output_dir = ""
left_filename = "left_dictionary.txt"
right_filename = "right_dictionary.txt"
# sample_dictionary = {"Name": "Bob", "Age": 28}

right_keys = get_right_keys()
left_keys = get_left_keys()
left_dic = get_key_connection_dictionary(
    abs_output_dir, left_filename, right_keys
)
right_dic = get_key_connection_dictionary(
    abs_output_dir, right_filename, left_keys
)
