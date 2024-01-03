"""Tests whether the adder function indeed adds 2 to a given input."""
import copy
import unittest
from typing import List

from typeguard import typechecked

from src.pythontemplate.debugging import list_faulty_wires

# Load fully connected keyboard half matrix dictionary.
from src.pythontemplate.hardcoded_wiring import hardcoded_rhs


class Test_adder(unittest.TestCase):
    """Object used to test a parse_creds function."""

    # Initialize test object
    @typechecked
    def __init__(self, *args, **kwargs):  # type:ignore[no-untyped-def]
        super().__init__(*args, **kwargs)

    @typechecked
    def test_no_unconnected_wires(self) -> None:
        """Tests if list_faulty_wires returns an empty list if all keys are
        connected and recognised successfully."""
        actual_error_messages: List[str] = list_faulty_wires(
            keyboard_half_dict=hardcoded_rhs, is_left=False
        )
        expected_error_messages: List[str] = []
        self.assertEqual(actual_error_messages, expected_error_messages)

    @typechecked
    def test_f8_not_connected(self) -> None:
        """Tests if list_faulty_wires returns an empty list if all keys are
        connected and recognised successfully."""
        # Create keyboard matrix with unconnected wire.
        faulty_matrix = copy.deepcopy(hardcoded_rhs)
        faulty_matrix["F8"] = (None, None)

        # Get the hardcoded data of the F8 key wiring.
        # 4,15, left half
        # Wire(15, "gray", 17),
        # Wire(4, "yellow", 6),

        # Create expected error message.
        first_error_message = (
            "For key:F8, the Raspberry Pico GPIO pin number: 4"
            + " is not connected to Raspberry Pico GPIO pin number: "
            + str(15)
            + ". "
            "This means the yellow wire from the Raspberry Pico GPIO "
            "pin number: 4 is not connected to"
            " the GPIO pin on the right side of the keyboard with the number:"
            " 6, "
            "Or that the gray wire from the Raspberry Pico GPIO "
            "pin number: 15 is not connected to"
            " the GPIO pin on the right side of the keyboard with the number:"
            " 17. Or both."
        )

        actual_error_messages: List[str] = list_faulty_wires(
            keyboard_half_dict=faulty_matrix, is_left=False
        )
        expected_error_messages: List[str] = [first_error_message]
        self.assertEqual(
            len(actual_error_messages), len(expected_error_messages)
        )
        for actual_error_message, expected_error_message in zip(
            actual_error_messages, expected_error_messages
        ):
            print("actual_error_message=")
            print(actual_error_message)
            print("expected_error_message=")
            print(expected_error_message)
            self.assertEqual(actual_error_message, expected_error_message)


if __name__ == "__main__":
    unittest.main()
