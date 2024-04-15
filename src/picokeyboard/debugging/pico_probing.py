"""Contains the functions to probe the pico to see if any GPIO pins are
connected to each other.

If they are it implies a key is being pressed.
"""

import digitalio

from src.picokeyboard.wiring.get_gpio_pin_nrs import (
    get_pico_gpio_pin_nrs,
    pin_to_board_pin,
)


def get_connected_pins_per_key():
    """Loops over all the pins in the Pico, and then if there is a connection
    between any of them.

    If yes, it implies a key is being pressed that is the
    bridge/switch/connector between those two GPIO pins on the Pico.
    """
    for left in get_pico_gpio_pin_nrs():
        for right in get_pico_gpio_pin_nrs():
            if left != right:
                print(f"check: left={left},right={right}")
                has_connection = (
                    detect_connection_between_two_pins_circuitpythonV5(
                        left, right
                    )
                )

                # print(f"has_connection={has_connection}")
                if has_connection:
                    return left, right
    return None, None


def detect_connection_between_two_pins_circuitpythonV5(left, right):
    """Detects if there is a connection between two GPIO pins on the Pico."""
    out = digitalio.DigitalInOut(pin_to_board_pin(left))
    out.direction = digitalio.Direction.OUTPUT
    out.value = 1

    input_signal = digitalio.DigitalInOut(pin_to_board_pin(right))
    input_signal.direction = digitalio.Direction.INPUT
    input_signal.pull = digitalio.Pull.DOWN

    # Check if the input_signal has an incoming value.
    if input_signal.value:
        out.deinit()
        input_signal.deinit()
        return True
    # row.value = 0
    out.deinit()
    input_signal.deinit()
    return False
