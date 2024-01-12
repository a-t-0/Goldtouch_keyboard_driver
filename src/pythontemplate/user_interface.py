"""This module does the talking to the user."""


def ask_user_to_press_pin(key):
    """Ask the user to press a key on the keyboard that is being tested."""
    val = input(
        f"On the keyboard that you are testing: press and hold: {key}, Press"
        + " <enter> with your normal keyboard in this terminal to start "
        + f"scanning>, hold: {key} until we say: done ."
    )
    print(val)


def print_matrix(connected_pins_per_key, rows):
    """Prints the keyboard matrix to the terminal in the format:
    <key>: <left GPIO pin on Pico>, <right GPIO pin on Pico>"""
    for row in rows:
        new_line = ""
        for key in row:
            new_line = f"{new_line}  {key}: {connected_pins_per_key[key]}"
        print(new_line)
    print("\n Here is a version to copy-paste into the code:")
    print(connected_pins_per_key)
    print("")
    return connected_pins_per_key


def ask_user_to_get_left_or_right_half(half):
    """Ask the user to press the left or right half of the keyboard."""
    get_half = input(
        f"Do you want to get the connection matrix for the {half} half? (y/n)"
    )
    if get_half == "y":
        return True
    if get_half == "n":
        return False
    print("Please enter y or n")
    return ask_user_to_get_left_or_right_half(half)


def print_messages(messages):
    """Prints the messages to the terminal."""
    for message in messages:
        print(message)
