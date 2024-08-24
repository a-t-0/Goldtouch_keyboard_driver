"""Entry point for the project."""

# from argparse import Namespace

# from typeguard import typechecked

# from src.picokeyboard.argparser import parse_args
from src.picokeyboard.code_generator.generate_kmk_main import generate_kmk_main
from src.picokeyboard.code_generator.output_kmk_main import output_kmk_main

rel_wiring_filepath: str = "output/wiring_scheme.py"
kmk_main_rel_filepath: str = "keyboard_driver/main.py"
# args: Namespace = parse_args()

store_wiring = False
debug_wiring = False
create_keybaord_driver = True
install = False
use = False
# @typechecked
# def process_args(*, args: Namespace, rel_wiring_filepath: str) -> None:
# """Calls the functions that are requested in the args."""
if store_wiring:
    from src.picokeyboard.wiring.generate_wiring_scheme import (
        generate_wiring_scheme_if_not_exists,
    )

    generate_wiring_scheme_if_not_exists(filepath=rel_wiring_filepath)
elif debug_wiring:
    from src.picokeyboard.debugging.debugging import debug_keyboard_keys

    debug_keyboard_keys()
elif create_keybaord_driver:
    keyboard_driver_main: str = generate_kmk_main()
    output_kmk_main(
        keyboard_driver_main=keyboard_driver_main,
        kmk_main_rel_filepath=kmk_main_rel_filepath,
    )
elif install:
    # If this code is not ran on the Pico, generate the Python code that
    # creates the KMK main.py file/driver for the keyboard.
    print(
        "TODO: copy the relevant files into the Pico, and verify the"
        " prerequisites are satisfied."
    )
elif use:
    print("TODO: launch the keyboard.")
else:
    raise SystemError(
        "This code should not be reached, the argparser should have"
        " asserted at least one CLI argument option is selected."
    )
