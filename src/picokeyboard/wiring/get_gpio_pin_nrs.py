"""Stores a list of all GPIO pin numbers of the Raspberry Pi Pico."""

try:
    import board  # circuitpython only
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Was not able to import module named 'board', which is probably thrown"
        " because you are not running this from thonny and/or not from the "
        "Pico (within Thonny)"
    ) from None


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
