"""This code automatically generates the Python code that creates the KMK
main.py file/driver for the keyboard."""


from src.pythontemplate.debugging import get_rows_and_cols
from src.pythontemplate.hardcoded_wiring import hardcoded_lhs, hardcoded_rhs


def generate_kmk_main():
    """This code automatically generates the Python code that creates the KMK
    main.py file/driver for the keyboard."""

    part_0 = """print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO
"""
    rows, cols = get_merged_rows_and_cols()
    # rows=[0,1,2,3,4,5,7,16]
    # cols=[8,11,12]
    col_pins = []
    row_pins = []
    for row in rows:
        row_pins.append(f"board.GP{row}")
    for col in cols:
        col_pins.append(f"board.GP{col}")

    # keyboard.col_pins = (board.GP0,)
    # keyboard.row_pins = (board.GP1,)
    col_pins_str = "("
    for i in range(len(col_pins)):
        col_pins_str += f"{col_pins[i]}, "
    col_pins_str += ")"

    row_pins_str = "("
    for i in range(len(row_pins)):
        # row_pins_str+=row_pins[i]
        row_pins_str += f"{row_pins[i]}, "
    row_pins_str += ")"

    part_1 = f"keyboard.row_pins = {row_pins_str}"
    part_2 = f"keyboard.col_pins = {col_pins_str}"
    part_3 = """keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = ["""

    kmk_key_matrix = generate_main_key_map(rows=rows, cols=cols)
    kmk_key_str = kmk_key_matrix_to_str(kmk_key_matrix)
    part_4 = """]
if __name__ == '__main__':
    keyboard.go()"""

    merged_code = (
        part_0
        + "\n"
        + part_1
        + "\n"
        + part_2
        + "\n"
        + part_3
        + kmk_key_str
        + part_4
    )
    print(merged_code)


def generate_main_key_map(rows, cols):
    """Loops through the hardcoded_rhs and hardcoded_lhs to generate the KMK
    keymap."""
    kmk_key_matrix = initialise_matrix(len(rows), len(cols))
    for i, row in enumerate(rows):
        for j, col in enumerate(cols):
            if row != col:
                found_key = False
                for key, value in hardcoded_lhs.items():
                    if value == (row, col):
                        found_key = True
                        kmk_key_matrix[i][j] = f"KC.{key}"
                for key, value in hardcoded_rhs.items():
                    if value == (row, col):
                        if not found_key:
                            found_key = True
                            kmk_key_matrix[i][j] = f"KC.{key}"
                if not found_key:
                    # TODO: replace with permissible empty value.
                    kmk_key_matrix[i][j] = "KC._______"
    return kmk_key_matrix


def initialise_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("KC._______")
        matrix.append(row)
    return matrix


def get_merged_rows_and_cols():
    """Returns the unique rows and columns of the Pico GPIO pins."""
    left_rows, left_cols = get_rows_and_cols(hardcoded_lhs, is_left=True)
    right_rows, right_cols = get_rows_and_cols(hardcoded_rhs, is_left=False)
    rows = list(set(left_rows + right_rows))
    cols = list(set(left_cols + right_cols))
    return rows, cols


def kmk_key_matrix_to_str(kmk_key_matrix):
    """Converts the KMK key matrix to a string."""
    matrix_str = "["
    for row in kmk_key_matrix:
        for key_name in row:
            matrix_str += key_name + ", "
    matrix_str += "]"
    return matrix_str
