"""Parses the CLI args for this repository."""

import argparse
from argparse import ArgumentParser, Namespace
from typing import List

# from typeguard import typechecked


# @typechecked
def parse_args() -> Namespace:
    """Creates the argument parser object and returns the parsed arguments."""
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Create your Raspberry Pico keyboard driver."
    )  # Add an argument
    parser.add_argument(
        "--store-wiring",
        type=bool,
        default=False,
        required=False,
    )
    parser.add_argument(
        "--debug-wiring", type=bool, default=False, required=False
    )

    parser.add_argument("--install", type=bool, default=False, required=False)
    parser.add_argument("--use", type=bool, default=False, required=False)
    args: Namespace = parser.parse_args()
    assert_only_one_action_is_asked(
        arglist=[args.store_wiring, args.debug_wiring, args.install, args.use]
    )
    return args


# @typechecked
def assert_only_one_action_is_asked(*, arglist: List[bool]) -> None:
    """Ensures the user only asks to do one thing."""
    if sum(arglist) > 1:
        raise AssertionError("More than 1 arg option is not supported.")
