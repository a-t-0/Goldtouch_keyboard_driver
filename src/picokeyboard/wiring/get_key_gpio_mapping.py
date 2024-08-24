"""Contains functions that read out how the GPIO pins on the Raspberry Pico are
connected through key-presses."""

from src.picokeyboard.debugging.pico_probing import get_connected_pins_per_key
from src.picokeyboard.ask_user.user_interface import (  # circuitpython only
    ask_user_to_press_pin,
    print_matrix,
)


def create_emtpy_pin_connection_matrix_dictionary(*, rows):
    """Creates an empty dictionary to store a tuple of two integers
    representing the two GPIO pin numbers on the Raspberry Pico, for each key
    in the keyboard matrix."""
    connected_pins_per_key = {}
    for row in rows:
        for key in row:
            connected_pins_per_key[key] = None
    return connected_pins_per_key


def store_pin_connection_pairs_per_key(rows):
    """Ask the user to press each key and store the connected pins in a
    dictionary."""
    connected_pins_per_key = create_emtpy_pin_connection_matrix_dictionary(
        rows=rows
    )
    for row in rows:
        for key in row:
            ask_user_to_press_pin(key)
            left, right = get_connected_pins_per_key()
            connected_pins_per_key[key] = (left, right)
            if left is not None and right is not None:
                print(f"Done, got for key:{key} left={left},right={right}")
            else:
                print(f"Failed for key:{key} left={left},right={right}")
    print("matrix")
    print_matrix(connected_pins_per_key, rows)
    return connected_pins_per_key


def get_key_connection_dictionary(keys):
    """Get the connection between the pins for each key and store it in a
    dictionary."""

    # Get the circuitpython pins:
    # Ask user to press keys to get the keyboard wirign connection matrix
    connected_pins_per_key = store_pin_connection_pairs_per_key(keys)

    return connected_pins_per_key
