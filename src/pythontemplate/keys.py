"""Store the key layout for the keyboard.

Assumes a split keyboard.
"""


def get_right_keys():
    """Start at top left.

    Go Western reading, first left to right, then top to bottom.
    """
    rows = []
    row_0 = [
        "F8",
        "F9",
        "F10",
        "F11",
        "F12",
        "SCROLL_LOCK",
        "INSERT",
        "DELETE",
    ]
    row_1 = [
        "7",
        "8",
        "9",
        "0",
        "MINUS",
        "EQUAL",
        "BACKSPACE",
        "BSPC",
    ]
    row_2 = [
        "Y",
        "U",
        "I",
        "O",
        "P",
        "LBRACKET",
        "RBRACKET",
        "BACKSLASH",
    ]
    row_3 = [
        "H",
        "J",
        "K",
        "L",
        "SEMICOLON",
        "QUOTE",
        "ENTER",
        "ENT",
    ]
    row_4 = [
        "N",
        "m",
        "COMMA",
        "DOT",
        "SLASH",
        "RIGHT_SHIFT",
        "UP",
        "PRINT_SCREEN",
    ]
    row_5 = [
        "SPACE",
        "SPC",
        "RIGHT_ALT",
        "RIGHT_SUPER",
        "RIGHT_CONTROL",
        "LEFT",
        "DOWN",
        "RIGHT",
    ]

    rows.append(row_0)
    rows.append(row_1)
    rows.append(row_2)
    rows.append(row_3)
    rows.append(row_4)
    rows.append(row_5)

    return rows


def get_left_keys():
    """Start at top left.

    Go Western reading, first left to right, then top to # bottom.
    """
    rows = []
    row_0 = [
        "ESCAPE",
        "F1",
        "F2",
        "F3",
        "F4",
        "F5",
        "F6",
        "F7",
    ]
    row_1 = [
        "HOME",
        "GRAVE",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
    ]
    row_2 = [
        "PGUP",
        "TAB",
        "TAB",
        "Q",
        "W",
        "E",
        "R",
        "T",
    ]
    row_3 = [
        "PGDOWN",
        "CAPS_LOCK",
        "CAPSLOCK",
        "A",
        "S",
        "D",
        "F",
        "G",
    ]
    row_4 = [
        "END",
        "LEFT_SHIFT",
        "LSHIFT",
        "Z",
        "X",
        "C",
        "V",
        "B",
    ]
    row_5 = [
        "FN",
        "LEFT_CONTROL",
        "LCTRL",
        "LEFT_SUPER",
        "LEFT_ALT",
        "SPACE",
        "SPC",
        "SPACE",
    ]

    rows.append(row_0)
    rows.append(row_1)
    rows.append(row_2)
    rows.append(row_3)
    rows.append(row_4)
    rows.append(row_5)

    return rows
