"""Stores a list of all GPIO pin numbers of the Raspberry Pi Pico."""


def get_pico_gpio_pin_nrs():
    """Returns a list of all GPIO pin numbers of the Raspberry Pi Pico."""
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
    """Creates an empty dictionary to store a tuple of two integers
    representing the two GPIO pin numbers on the Raspberry Pico, for each key
    in the keyboard matrix."""
    connected_pins_per_key = {}
    for row in rows:
        for key in row:
            connected_pins_per_key[key] = None
    return connected_pins_per_key
