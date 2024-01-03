"""Helps the user identify which wire connection is not working properly, if
any."""
from src.pythontemplate.hardcoded_wiring import (
    hardcoded_lhs,
    hardcoded_lhs_wires,
    hardcoded_rhs,
    hardcoded_rhs_wires,
)


def get_keyboard_half_pin_key_matrix(keyboard_half_dict, is_left):
    """Returns the dictionary with the GPIO pin numbers for the back connector
    of the half of the keyboard.

    TODO: write test for this function.
    """
    back_half_key_matrix = {}
    if is_left:
        expected_wires = hardcoded_lhs_wires
    else:
        expected_wires = hardcoded_rhs_wires

    for key, value in keyboard_half_dict.items():
        if value == (None, None):
            raise ValueError("The key matrix is not complete.")
        # Get the relevant wire based on keymatrix.
        left_wire, right_wire = get_wire(
            keyboard_half_dict[key], expected_wires
        )
        back_half_key_matrix[key] = (
            left_wire.keyboard_pin_nr,
            right_wire.keyboard_pin_nr,
        )
    return back_half_key_matrix


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
