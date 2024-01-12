"""Contains the functions to probe the pico to see if any GPIO pins are
connected to each other.

If they are it implies a key is being pressed.
"""
import board  # circuitpython only
import digitalio

from src.pythontemplate.gpio_pin_nrs import get_pico_gpio_pin_nrs


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


# pylint: disable=R0911,R0912
def pin_to_board_pin(pin_nr):
    """Converts a pin number to a Pico board pin object."""
    if pin_nr == 0:
        return board.GP0
    if pin_nr == 1:
        return board.GP1
    if pin_nr == 2:
        return board.GP2
    if pin_nr == 3:
        return board.GP3
    if pin_nr == 4:
        return board.GP4
    if pin_nr == 5:
        return board.GP5
    if pin_nr == 6:
        return board.GP6
    if pin_nr == 7:
        return board.GP7
    if pin_nr == 8:
        return board.GP8
    if pin_nr == 9:
        return board.GP9
    if pin_nr == 10:
        return board.GP10
    if pin_nr == 11:
        return board.GP11
    if pin_nr == 12:
        return board.GP12
    if pin_nr == 13:
        return board.GP13
    if pin_nr == 14:
        return board.GP14
    if pin_nr == 15:
        return board.GP15
    if pin_nr == 16:
        return board.GP16
    if pin_nr == 17:
        return board.GP17
    if pin_nr == 18:
        return board.GP18
    if pin_nr == 19:
        return board.GP19
    if pin_nr == 20:
        return board.GP20
    if pin_nr == 21:
        return board.GP21
    if pin_nr == 22:
        return board.GP22
    if pin_nr == 23:
        return board.GP23
    if pin_nr == 24:
        return board.GP24
    if pin_nr == 25:
        return board.GP25
    if pin_nr == 26:
        return board.GP26
    if pin_nr == 27:
        return board.GP27
    if pin_nr == 28:
        return board.GP28
    raise SystemError(f"No  pin found for: pin_nr={pin_nr}.")
