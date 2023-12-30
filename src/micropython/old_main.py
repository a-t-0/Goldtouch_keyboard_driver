print("Hello World!")
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,board.GP18,board.GP19,board.GP20,board.GP21,board.GP22,board.GP26,board.GP27)    # try D5 on Feather, keeboar
#keyboard.row_pins = (board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,board.GP17,board.GP18,board.GP19,board.GP20,board.GP21,board.GP22)    # try D6 on Feather, keeboar
keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7)
#keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.diode_orientation = DiodeOrientation.ROW2COL
# Preload unshifted keys (Avoids stack
keyboard.keymap = [
    [
        KC.N0,KC.N0,KC.LEFT,KC.SPACE,KC.N0,KC.SCROLL_LOCK,KC.RIGHT_CONTROL,KC.N0,KC.N3,KC.N0,KC.B,KC.F3,KC.C,KC.D,KC.E,KC.F2,\
        KC.N0,KC.N0,KC.RIGHT,KC.PRINT_SCREEN,KC.F12,KC.INSERT,KC.N0,KC.RIGHT_ALT,KC.N2,KC.T,KC.S,KC.W,KC.X,KC.N0,KC.CAPSLOCK,KC.F1,\
        KC.RIGHT_SUPER,KC.N0,KC.BACKSPACE,KC.N0,KC.F10,KC.F9,KC.N0,KC.N0,KC.RIGHT_CONTROL,KC.N0,KC.N0,KC.LEFT_SHIFT,KC.N0,KC.N0,KC.SPC,KC.N0,\
        KC.N0,KC.RIGHT_SHIFT,KC.DOWN,KC.ENT,KC.F11,KC.DELETE,KC.N0,KC.N0,KC.N4,KC.N0,KC.N0,KC.N6,KC.V,KC.F,KC.R,KC.N5,\
        KC.LBRACKET,KC.SEMICOLON,KC.SLASH,KC.P,KC.N0,KC.MINUS,KC.N0,KC.QUOTE,KC.PGUP,KC.N0,KC.LEFT_SUPER,KC.N0,KC.N0,KC.N0,KC.F5,KC.G,\
        KC.Y,KC.H,KC.N,KC.U,KC.N7,KC.N0,KC.M,KC.J,KC.PGDOWN,KC.N0,KC.N0,KC.N0,KC.LEFT_ALT,KC.N0,KC.F7,KC.F4,\
        KC.RBRACKET,KC.BACKSLASH,KC.N0,KC.I,KC.N8,KC.EQUAL,KC.COMMA,KC.K,KC.N1,KC.N0,KC.ESCAPE,KC.TAB,KC.Z,KC.A,KC.Q,KC.GRAVE,\
        KC.N0,KC.N0,KC.UP,KC.O,KC.N9,KC.F8,KC.DOT,KC.L,KC.N0,KC.N0,KC.N0,KC.N0,KC.N0,KC.N0,KC.N0,KC.N0,\
    ]
]


if __name__ == '__main__':
    keyboard.go()