"""Helps the user identify which wire connection is not working properly, if
any."""
from src.pythontemplate.hardcoded_wiring import hardcoded_lhs, hardcoded_rhs,lhs_wires,rhs_wires


def list_faulty_wires(keyboard_half_dict, is_left):
    """List the wires that are not connected properly."""

    if is_left:
        expected_keymatrix = hardcoded_lhs
        expected_wiring_list=lhs_wires
    else:
        expected_keymatrix = hardcoded_rhs
        expected_wiring_list=lhs_wires
    print("Left half:")
    for key, value in keyboard_half_dict.items():
        if value == (None, None):
            print(
                f"For key:{key}, the Raspberry Pico GPIO pin number:\n"
                + expected_keymatrix[key][0]
                + "is not connected to Raspberry Pico GPIO pin number:\n"
                + expected_keymatrix[key][1]
            )
            # TODO: get the relevant wire based on keymatrix.
            print("This means the {colour} wire from the Raspberry Pico GPIO "
                  "pin number:\n"
                  + expected_keymatrix[key][0]
                  )
            # TODO: finish print statement, then test print statement.
