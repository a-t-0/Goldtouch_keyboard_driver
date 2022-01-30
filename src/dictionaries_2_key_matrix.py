# Imports dictonary and generates the keymatrix
right_dic = {
    "I": (6, 11),
    "H": (5, 9),
    "K": (6, 15),
    "J": (5, 15),
    "U": (5, 11),
    "ENT": (3, 11),
    "LBRACKET": (4, 8),
    "SPACE": (0, 11),
    "F9": (2, 13),
    "P": (4, 11),
    "SEMICOLON": (4, 9),
    "BACKSLASH": (6, 9),
    "RIGHT_SHIFT": (3, 9),
    "F8": (7, 13),
    "RIGHT_SUPER": (2, 8),
    "SLASH": (4, 10),
    "Y": (5, 8),
    "F12": (1, 12),
    "ENTER": (3, 11),
    "RIGHT_CONTROL": (0, 14),
    "BACKSPACE": (2, 10),
    "F10": (2, 12),
    "F11": (3, 12),
    "M": (5, 14),
    "BSPC": (2, 10),
    "O": (7, 11),
    "RIGHT": (1, 10),
    "N7": (5, 12),
    "DELETE": (3, 13),
    "N0": (4, 12),
    "DOT": (7, 14),
    "SCROLL_LOCK": (0, 13),
    "INSERT": (1, 13),
    "N9": (7, 12),
    "N8": (6, 12),
    "LEFT": (0, 10),
    "RBRACKET": (6, 8),
    "QUOTE": (4, 15),
    "UP": (7, 10),
    "PRINT_SCREEN": (1, 11),
    "MINUS": (4, 13),
    "RIGHT_ALT": (1, 15),
    "EQUAL": (6, 13),
    "SPC": (0, 11),
    "DOWN": (3, 10),
    "COMMA": (6, 14),
    "L": (7, 15),
    "N": (5, 10),
}
left_dic = {
    "SPC": (2, 26),
    "LCTRL": (None, None),
    "LEFT_SHIFT": (2, 20),
    "N5": (3, 27),
    "N4": (3, 16),
    "T": (1, 18),
    "N1": (6, 16),
    "ESCAPE": (6, 19),
    "N3": (0, 16),
    "N2": (1, 16),
    "W": (1, 20),
    "Q": (6, 26),
    "S": (1, 19),
    "R": (3, 26),
    "CAPSLOCK": (1, 26),
    "CAPS_LOCK": (1, 26),
    "LSHIFT": (2, 20),
    "F3": (0, 20),
    "PGDOWN": (5, 16),
    "F2": (0, 27),
    "GRAVE": (6, 27),
    "F7": (5, 26),
    "F6": (None, None),
    "F5": (4, 26),
    "F4": (5, 27),
    "PGUP": (4, 16),
    "TAB": (6, 20),
    "F1": (1, 27),
    "X": (1, 21),
    "HOME": (None, None),
    "Z": (6, 21),
    "N6": (3, 20),
    "V": (3, 21),
    "ASTERISK": (2, 16),
    "LEFT_CONTROL": (None, None),
    "E": (0, 26),
    "D": (0, 22),
    "G": (4, 27),
    "F": (3, 22),
    "A": (6, 22),
    "LEFT_SUPER": (4, 19),
    "END": (None, None),
    "C": (0, 21),
    "B": (0, 19),
    "LEFT_ALT": (5, 21),
    "SPACE": (2, 26),
}


def replace_dic_key(left_dic, right_dic, new_key, old_key):
    try:
        left_dic[new_key] = left_dic.pop(old_key)
        right_dic[new_key] = right_dic.pop(old_key)
    except:
        pass
    return left_dic, right_dic


# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "LCTRL")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "ENT")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "LEFT_SHIFT")
left_dic, right_dic = replace_dic_key(
    left_dic, right_dic, "N1", "ASTERISK"
)  # causes pystack exausted
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")
# left_dic, right_dic = replace_dic_key(left_dic, right_dic, "N0", "")

# filler="'____'"
filler = "____"
filler = "KC.N0"


def get_rows():
    pin_nrs = [0, 1, 2, 3, 4, 5, 6, 7]
    return pin_nrs


def get_columns():
    pin_nrs = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 26, 27, 28]
    return pin_nrs


def get_used_cols(dic):
    used_left = []
    used_right = []
    for i in range(0, 29):
        for key, value in dic.items():
            left = value[0]
            right = value[1]
            # print(key, '->', value)
            # print(f"left={left},right={right}")
            if i == left:
                used_left.append(i)
            if i == right:
                used_right.append(i)
    return list(set(used_left)), list(set(used_right))


def get_matrix_element(row, gpio_col, left_dic, right_dic, filler):
    if get_matrix_element_for_dic(row, gpio_col, left_dic, filler) == filler:
        return get_matrix_element_for_dic(row, gpio_col, right_dic, filler)
    else:
        return get_matrix_element_for_dic(row, gpio_col, left_dic, filler)


def get_matrix_element_for_dic(row, gpio_col, dic, filler):
    for key, value in dic.items():
        left = value[0]
        right = value[1]
        # print(key, '->', value)
        # print(f"left={left},right={right}")
        if row == left:
            if gpio_col == right:
                # print(f'Returning:{key}')
                return key
    return filler


rows, columns = 8, 16
# rows, columns = 4, 4
matrix = [[filler for x in range(rows)] for y in range(columns)]

left_used_left, left_used_right = get_used_cols(left_dic)
# print(f"left_used_left={left_used_left},left_used_right={left_used_right}")
right_used_left, right_used_right = get_used_cols(right_dic)
# print(f"right_used_left={right_used_left},right_used_right={right_used_right}")
right_gpios = right_used_right
right_gpios.extend(left_used_right)
print(f"right_gpios={right_gpios}")
print(f"len right_gpios={len(right_gpios)}")

# generate keyboard rows
line = "keyboard.row_pins = ("
for pin in right_gpios:
    line = f"{line}board.GP{pin},"
line = f"{line})"
print(line)

# Generate key matrix
for row in range(0, rows):
    for col in range(0, columns):
        gp_row = get_rows()[row]
        gp_col = get_columns()[col]
        # print(f"row={row},gp_row={gp_row},col={col},gp_col={gp_col}")
        matrix[col][row] = get_matrix_element(
            row, right_gpios[col], left_dic, right_dic, filler
        )

# Output copyable matrix python code
print(matrix)
print("")
print("")
print("keyboard.keymap = [")
print("    [")
for row in range(0, rows):
    line = "        "
    for col in range(0, columns):
        if matrix[col][row] == filler:
            element = matrix[col][row]
        else:
            element = f"KC.{matrix[col][row]}"
        if col == 0:
            line = f"{line}{element}"
        else:
            line = f"{line},{element}"
    line = f"{line},\\"
    print(line)
print("    ]")
print("]")

# print rotated key matrix
print("")
print(
    "Note this contains an unexplainable slash after 8-ish elements. Also, it has the incorrect rotation."
)
print("keyboard.keymap = [")
print("    [")
for col in range(0, columns):
    for row in range(0, rows):
        if matrix[col][row] == filler:
            element = matrix[col][row]
        else:
            element = f"KC.{matrix[col][row]}"
        line = f"{line}{element},"
print(line)
print("    ]")
print("]")
