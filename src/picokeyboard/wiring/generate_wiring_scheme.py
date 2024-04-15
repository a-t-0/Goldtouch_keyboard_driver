"""Manages generating and exporting the wiring scheme.

The wiring scheme is a dictionary that contains the primary keys on the
keyboard as keys, and the GPIO pin pairs (in and out) of the Raspberry
Pico that correspond to this key.
"""

from typeguard import typechecked

from src.picokeyboard.debugging.debugging import list_faulty_wires
from src.picokeyboard.hardcoded.keys import (
    load_hardcoded_left_keys,
    load_hardcoded_right_keys,
)
from src.picokeyboard.user_interface import (
    ask_user_to_get_left_or_right_half,
    print_messages,
)
from src.picokeyboard.wiring.get_key_gpio_mapping import (
    get_key_connection_dictionary,
)


@typechecked
def generate_wiring_scheme_if_not_exists(*, filepath: str) -> None:
    """Creates the wiring scheme if it does not yet exist.

    Otherwise throws error. It asks the user to press each key in the
    keyboard, and then scans the Raspberry Pico connections to determine
    which connection corresponds to which port.
    """
    right_keys = load_hardcoded_right_keys()
    left_keys = load_hardcoded_left_keys()

    # This asks you to press the keys, then it scans all GPIO ports on the
    # Raspberry Pico, and determines which two GPIO pins connect which key on
    # the keyboard.
    if ask_user_to_get_left_or_right_half("left"):
        left_dic = get_key_connection_dictionary(left_keys)
        print_messages(messages=list_faulty_wires(left_dic, True))
    if ask_user_to_get_left_or_right_half("right"):
        right_dic = get_key_connection_dictionary(right_keys)
        print_messages(messages=list_faulty_wires(right_dic, False))

    # TODO: assert the dictionaries are complete (e.g. no faulty wiring), and
    # raise warning otherwise.
    # TODO: export left and right dict.


@typechecked
def wiring_scheme_exists(filename: str) -> bool:
    """Returns True if the wiring scheme already exists, false otherwise."""


@typechecked
def delete_wiring_scheme(filename: str) -> bool:
    """Asserts the wiring scheme exists, and then deletes it.

    Then asserts it does not exist.
    """


@typechecked
def export_wiring_scheme(filename: str) -> None:
    """Exports the created wiring scheme to file.

    Then asserts the wiring scheme exists.
    """
    # Implement logic to import wiring scheme from filename


@typechecked
def import_wiring_scheme(filename: str) -> None:
    # Implement logic to import wiring scheme from filename
    pass
