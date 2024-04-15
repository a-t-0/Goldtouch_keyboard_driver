"""Helps the user identify which wire connection is not working properly, if
any."""

from src.picokeyboard.ask_user.user_interface import (
    ask_user_to_get_left_or_right_half,
    print_messages,
)
from src.picokeyboard.hardcoded.keys import (
    load_hardcoded_left_keys,
    load_hardcoded_right_keys,
)
from src.picokeyboard.wiring.get_key_gpio_mapping import (
    get_key_connection_dictionary,
)
from src.picokeyboard.wiring.hardcoded_wiring import (
    hardcoded_lhs,
    hardcoded_lhs_wires,
    hardcoded_rhs,
    hardcoded_rhs_wires,
)


def debug_keyboard_keys() -> None:
    """Loads the wiring scheme, then asks the user to press each key, and then
    prints which wires are not wired correctly."""

    right_keys = load_hardcoded_right_keys()
    left_keys = load_hardcoded_left_keys()
    if ask_user_to_get_left_or_right_half("left"):
        left_dic = get_key_connection_dictionary(left_keys)
        print_messages(messages=list_faulty_wires(left_dic, True))

    if ask_user_to_get_left_or_right_half("right"):
        right_dic = get_key_connection_dictionary(right_keys)
        print_messages(messages=list_faulty_wires(right_dic, False))

    # TODO: move this comment.
    # This asks you to press the keys, then it scans all GPIO ports on the
    # Raspberry Pico, and determines which two GPIO pins connect which key on
    # the keyboard.


def list_faulty_wires(keyboard_half_dict, is_left):
    """List the wires that are not connected properly."""

    error_messages = []
    if is_left:
        expected_keymatrix = hardcoded_lhs
        expected_wires = hardcoded_lhs_wires
        side = "left"
    else:
        expected_keymatrix = hardcoded_rhs
        expected_wires = hardcoded_rhs_wires
        side = "right"
    for key, value in keyboard_half_dict.items():
        if value == (None, None):
            part_one = (
                f"For key:{key}, the Raspberry Pico GPIO pin number: "
                + str(expected_keymatrix[key][0])
                + " is not connected to Raspberry Pico GPIO pin number: "
                + str(expected_keymatrix[key][1])
                + ". "
            )
            # Get the relevant wire based on keymatrix.
            left_wire, right_wire = get_wire(
                expected_keymatrix[key], expected_wires
            )
            part_two = (
                f"This means the {left_wire.colour} wire from the Raspberry "
                + f"Pico GPIO pin number: {left_wire.pico_pin_nr} is not "
                + f"connected to the GPIO pin on the {side} side of the "
                + "keyboard with the number: "
                + f"{left_wire.keyboard_pin_nr}, "
                + f"Or that the {right_wire.colour} wire from the Raspberry "
                + "Pico GPIO pin number: "
                + f"{right_wire.pico_pin_nr} is not connected to"
                + f" the GPIO pin on the {side} side of the keyboard with the "
                + f"number: {right_wire.keyboard_pin_nr}. Or both."
            )
            # TODO: finish print statement, then test print statement.
            error_messages.append(f"{part_one}{part_two}")
    return error_messages


def get_wire(gpio_pin_tuple, wires_list):
    """Returns the two Wire objects that are connected to the given GPIO pin
    tuple."""
    first_pin = gpio_pin_tuple[0]
    second_pin = gpio_pin_tuple[1]
    for wire in wires_list.wires:
        if wire.pico_pin_nr == first_pin:
            first_wire = wire
        if wire.pico_pin_nr == second_pin:
            second_wire = wire

    if first_wire is None or second_wire is None:
        raise ValueError("The wire could not be found.")
    if first_wire == second_wire:
        raise ValueError("The wire is connected to itself.")
    return first_wire, second_wire
