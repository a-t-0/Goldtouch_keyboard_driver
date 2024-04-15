print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Cleaner key names
_______ = KC.TRNS


keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, )
keyboard.col_pins = (board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP15, board.GP8, board.GP9, board.GP10, board.GP26, board.GP11, board.GP12, board.GP13, board.GP14, board.GP16, )
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[KC.N5, KC.N4, KC.N6, KC.V, KC.F, _______, KC.INSERT, KC.PGDOWN, KC.RIGHT, _______, _______, KC.RIGHT_ALT, _______, _______, KC.F12, KC.R, KC.F4, KC.PGDOWN, _______, KC.LEFT_ALT, _______, _______, KC.SCROLL_LOCK, KC.SPACE, KC.LEFT, KC.RIGHT_CONTROL, _______, _______, _______, _______, _______, KC.F7, _______, KC.FN, KC.LSHIFT, _______, _______, _______, KC.DELETE, KC.ENT, KC.DOWN, _______, _______, _______, KC.PGUP, _______, KC.F11, KC.SPC, KC.F2, KC.N3, KC.F3, KC.C, KC.D, _______, KC.F9, _______, KC.BSPC, _______, KC.B, _______, _______, KC.RIGHT_SUPER, KC.F10, KC.E, KC.G, KC.PGUP, _______, _______, _______, _______, KC.F8, KC.O, KC.UP, KC.DOT, KC.LEFT_SUPER, KC.L, _______, _______, KC.N9, KC.F5, KC.GRAVE, KC.N1, KC.TAB, KC.Z, KC.A, _______, KC.EQUAL, KC.I, _______, KC.COMMA, KC.ESCAPE, KC.K, KC.BACKSLASH, KC.RBRACKET, KC.N8, KC.Q, KC.F6, KC.HOME, _______, _______, KC.LEFT_CONTROL, _______, KC.MINUS, KC.P, KC.SLASH, _______, _______, KC.QUOTE, KC.SEMICOLON, KC.LBRACKET, KC.N0, KC.END, KC.F1, KC.N2, KC.W, KC.X, _______, KC.T, _______, KC.U, KC.N, KC.M, KC.S, KC.J, KC.H, KC.Y, KC.N7, KC.CAPS_LOCK, ]]
if __name__ == '__main__':
    keyboard.go()
