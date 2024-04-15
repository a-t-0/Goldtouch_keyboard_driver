"""Entry point for the project."""

from argparse import Namespace

from typeguard import typechecked

from src.picokeyboard.argparser import parse_args
from src.picokeyboard.debugging.debugging import debug_keyboard_keys
from src.picokeyboard.wiring.generate_wiring_scheme import (
    generate_wiring_scheme_if_not_exists,
)

rel_wiring_filepath: str = "output/wiring_scheme.py"
args: Namespace = parse_args()


@typechecked
def process_args(*, args: Namespace, rel_wiring_filepath: str) -> None:
    """Calls the functions that are requested in the args."""
    if args.store_wiring:
        generate_wiring_scheme_if_not_exists(filepath=rel_wiring_filepath)
    elif args.debug_wiring:
        debug_keyboard_keys()
    elif args.install:
        # If this code is not ran on the Pico, generate the Python code that
        # creates the KMK main.py file/driver for the keyboard.
        print(
            "TODO: copy the relevant files into the Pico, and verify the"
            " prerequisites are satisfied."
        )
    elif args.use:
        print("TODO: launch the keyboard.")
    else:
        raise SystemError(
            "This code should not be reached, the argparser should have"
            " asserted at least one CLI argument option is selected."
        )
