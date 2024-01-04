print("Starting")

import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP5, board.GP7, board.GP4)
keyboard.row_pins = (
    board.GP8,
    board.GP11,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[KC.I, KC.U, KC.O, KC.K, KC.J, KC.L]]
if __name__ == "__main__":
    keyboard.go()
