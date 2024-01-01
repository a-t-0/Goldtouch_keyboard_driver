def ask_user_to_press_pin(key):
    val = input(f"On the keyboard that you are testing: press and hold: {key}, Press <enter> with your normal keyboard in this terminal to start scanning>, hold: {key} untill we say: done .")
    print(val)

def print_matrix(connected_pins_per_key, rows):
    for row in rows:
        new_line = ""
        for key in row:
            new_line=f'{new_line}  {key}: {connected_pins_per_key[key]}'
            # print(f'{key}: {connected_pins_per_key[key]}')
        print(new_line)
        # print("")
    return connected_pins_per_key
