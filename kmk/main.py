print("Starting")

import board

from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

keyboard.row_pins = (
    board.GP8,
    board.GP9,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP11,
)
keyboard.col_pins = (board.GP16, board.GP17, board.GP18, board.GP19)
keyboard.diode_orientation = (
    DiodeOrientation.COL2ROW
)  # From Column to Rows, if you switch the polarity, it's ROW2COL

# Cleaner key names
_______ = KC.TRNS  # Transparent   -> Clicks through to previous layer
XXXXXXX = KC.NO  # No Action     -> Stops click through

FnKey = KC.MO(1)

VIDEO = send_string(
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
)  # Very important video

keyboard.keymap = [
    # Base Layer
    [
        KC.AUDIO_MUTE,
        KC.LCTL(KC.V),
        KC.BRIU,
        KC.AUDIO_VOL_UP,
        FnKey,
        KC.LCTL(KC.C),
        KC.BRID,
        KC.AUDIO_VOL_DOWN,
        KC.N7,
        KC.N8,
        KC.N9,
        KC.BSPACE,
        KC.N4,
        KC.N5,
        KC.N6,
        KC.ASTERISK,
        KC.N1,
        KC.N2,
        KC.N3,
        KC.PLUS,
        KC.N0,
        KC.DOT,
        KC.EQUAL,
        KC.ENTER,
    ],
    # Fn Layer
    [
        XXXXXXX,
        VIDEO,
        XXXXXXX,
        XXXXXXX,
        _______,
        XXXXXXX,
        XXXXXXX,
        XXXXXXX,
        _______,
        _______,
        _______,
        KC.DELETE,
        _______,
        _______,
        _______,
        KC.SLASH,
        _______,
        _______,
        _______,
        KC.MINUS,
        _______,
        KC.COMMA,
        _______,
        _______,
    ],
]

if __name__ == "__main__":
    keyboard.go()
