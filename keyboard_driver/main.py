print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, )
keyboard.col_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, )
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[KC.PGDOWN, KC.RIGHT, KC._______, KC.RIGHT_ALT, KC._______, KC._______, KC.F12, KC.INSERT, KC.N5, KC.R, KC.N4, KC.N6, KC.V, KC.F, KC._______, KC._______, KC.SPACE, KC.LEFT, KC.RIGHT_CONTROL, KC._______, KC._______, KC._______, KC._______, KC.SCROLL_LOCK, KC.G, KC.F5, KC.PGUP, KC._______, KC._______, KC._______, KC._______, KC.LEFT_SUPER, KC.ENT, KC.DOWN, KC._______, KC._______, KC.PGUP, KC._______, KC.F11, KC.DELETE, KC.F1, KC.CAPS_LOCK, KC.N2, KC.W, KC.X, KC._______, KC.T, KC.S, KC._______, KC.BACKSPACE, KC._______, KC._______, KC._______, KC.RIGHT_SUPER, KC.F10, KC.F9, KC.F6, KC.END, KC.HOME, KC._______, KC._______, KC.LEFT_CONTROL, KC._______, KC._______, KC.O, KC.UP, KC.DOT, KC.L, KC._______, KC._______, KC.N9, KC.F8, KC.F4, KC.F7, KC.PGDOWN, KC._______, KC.LEFT_ALT, KC._______, KC._______, KC._______, KC.I, KC._______, KC.COMMA, KC.K, KC.BACKSLASH, KC.RBRACKET, KC.N8, KC.EQUAL, KC.GRAVE, KC.Q, KC.N1, KC.TAB, KC.Z, KC.A, KC._______, KC.ESCAPE, KC.P, KC.SLASH, KC._______, KC.QUOTE, KC.SEMICOLON, KC.LBRACKET, KC.N0, KC.MINUS, KC._______, KC.SPACE, KC.FN, KC.LSHIFT, KC._______, KC._______, KC._______, KC._______, KC.U, KC.N, KC.m, KC.J, KC.H, KC.Y, KC.N7, KC._______, KC.F2, KC.E, KC.N3, KC.F3, KC.C, KC.D, KC._______, KC.B, ]]
if __name__ == '__main__':
    keyboard.go()