"""Stores the hardcoded wiring of the Goldtouch keyboard with a Raspberri
Pico."""


# pylint: disable=R0903
class Wire:
    """Stores a wire connection from the Raspberry Pico GPIO pins to the GPIO
    pin on the back of the half of the keyboard."""

    def __init__(self, pico_pin_nr, colour, keyboard_pin_nr):
        self.pico_pin_nr = pico_pin_nr
        self.colour = colour
        self.keyboard_pin_nr = keyboard_pin_nr

    def __repr__(self):
        return f"{self.pico_pin_nr}-{self.colour}-{self.keyboard_pin_nr}"


# pylint: disable=R0903
class Wires:
    """Stores a collection of wires from the Raspberry Pico GPIO pins to the
    GPIO pins on the back of the half of the keyboard."""

    def __init__(self, wires):
        self.wires = wires

    def __repr__(self):
        return "\n".join([str(wire) for wire in self.wires])


# This is the hardcoded dictionary with the GPIO pin numbers for the left half.
# So if you press the key 'a' on the left half, it will connect GPIO pin 5 and
# 10 on the Raspberry Pico.
hardcoded_lhs = {
    "I": (5, 8),
    "H": (7, 12),
    "K": (5, 11),
    "J": (7, 11),
    "U": (7, 8),
    "ENT": (2, 8),
    "LBRACKET": (6, 13),
    "SPACE": (1, 8),
    "F9": (3, 15),
    "P": (6, 8),
    "SEMICOLON": (6, 12),
    "BACKSLASH": (5, 12),
    "RIGHT_SHIFT": (2, 12),
    "F8": (4, 15),
    "RIGHT_SUPER": (3, 13),
    "SLASH": (6, 9),
    "Y": (7, 13),
    "F12": (0, 14),
    "ENTER": (2, 8),
    "RIGHT_CONTROL": (1, 10),
    "BACKSPACE": (3, 9),
    "F10": (3, 14),
    "F11": (2, 14),
    "m": (7, 10),
    "BSPC": (3, 9),
    "O": (4, 8),
    "RIGHT": (0, 9),
    "7": (7, 14),
    "DELETE": (2, 15),
    "0": (6, 14),
    "DOT": (4, 10),
    "SCROLL_LOCK": (1, 15),
    "INSERT": (0, 15),
    "9": (4, 14),
    "8": (5, 14),
    "LEFT": (1, 9),
    "RBRACKET": (5, 13),
    "QUOTE": (6, 11),
    "UP": (4, 9),
    "PRINT_SCREEN": (0, 8),
    "MINUS": (6, 15),
    "RIGHT_ALT": (0, 11),
    "EQUAL": (5, 15),
    "SPC": (1, 8),
    "DOWN": (2, 9),
    "COMMA": (5, 10),
    "L": (4, 11),
    "N": (7, 9),
}

hardcoded_rhs = {
    "SPC": (2, 6),
    "LCTRL": (17, 21),
    "LEFT_SHIFT": (2, 19),
    "5": (0, 7),
    "4": (0, 18),
    "T": (16, 22),
    "1": (5, 18),
    "ESCAPE": (5, 26),
    "3": (3, 18),
    "2": (16, 18),
    "W": (16, 19),
    "Q": (5, 6),
    "S": (16, 26),
    "R": (0, 6),
    "CAPSLOCK": (6, 16),
    "CAPS_LOCK": (6, 16),
    "LSHIFT": (2, 19),
    "F3": (3, 19),
    "PGDOWN": (1, 18),
    "F2": (3, 7),
    "GRAVE": (5, 7),
    "F7": (1, 6),
    "F6": (7, 17),
    "F5": (4, 6),
    "F4": (1, 7),
    "PGUP": (4, 18),
    "TAB": (5, 19),
    "F1": (7, 16),
    "X": (16, 20),
    "HOME": (17, 18),
    "Z": (5, 20),
    "6": (0, 19),
    "V": (0, 20),
    "FN": (2, 18),
    "LEFT_CONTROL": (17, 21),
    "E": (3, 6),
    "D": (3, 21),
    "G": (4, 7),
    "F": (0, 21),
    "A": (5, 21),
    "LEFT_SUPER": (4, 26),
    "END": (6, 17),
    "C": (3, 20),
    "B": (3, 26),
    "LEFT_ALT": (1, 20),
    "SPACE": (2, 6),
}

# This describes how the left-hand side is wired.
# - Skipping 0,1 18,19 on the flat connector because the outer 2 pins on each
#   end of the flat connector on the back of the keyboard half are unused.
# - As seen from front of the keyboard, with the flat connector at the bottom,
#   GPIO pins on top, from left to right on the chip.
# - Note there are double connections at GPIO pins 0 to 7, the LHS uses the top
#   row of these wires.
#  <GPIO pin nr on Pico> - wire colour - <GPIO pin nr on keyboard LHS>
lhs_wires = Wires(
    [
        Wire(0, "blue", 5),
        Wire(1, "green", 4),
        Wire(2, "black", 6),
        Wire(3, "brown", 7),
        Wire(4, "purple", 3),
        Wire(5, "red", 2),
        Wire(6, "white", 16),
        Wire(7, "yellow", 17),
        # Then from top left to bottom left on Pico:
        Wire(16, "yellow", 8),
        Wire(17, "orange", 9),
        Wire(18, "red", 10),
        Wire(19, "brown", 11),
        Wire(20, "white", 15),
        Wire(21, "purple", 14),
        Wire(22, "blue", 13),
        Wire(26, "green", 12),
    ]
)


# This describes how the right-hand side is wired.

# - Skipping 0,1 18,19 on the flat connector because the outer 2 pins on each
#   end of the flat connector on the back of the keyboard half are unused.
# - As seen from back, with the flat connector at the bottom, GPIO pins on top,
#   from left to right on the chip.

# <GPIO pin nr on Pico> - wire colour - <GPIO pin nr on keyboard RHS>
rhs_wires = Wires(
    [
        Wire(0, "brown", 2),
        Wire(0, "brown", 2),
        Wire(1, "blue", 3),
        Wire(2, "purple", 4),
        Wire(3, "red", 5),
        Wire(4, "yellow", 6),
        Wire(5, "white", 7),
        Wire(6, "green", 8),
        Wire(7, "orange", 9),
        Wire(8, "white", 10),
        Wire(9, "black", 11),
        Wire(10, "brown", 12),
        Wire(11, "red", 13),
        Wire(12, "orange", 14),
        Wire(13, "yellow", 15),
        Wire(14, "green", 16),
        Wire(15, "gray", 17),
    ]
)
