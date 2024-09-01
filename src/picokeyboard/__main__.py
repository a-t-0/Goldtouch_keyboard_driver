"""Entry point for the project."""

# try:
from src.picokeyboard.code_generator.generate_kmk_main import (
    generate_kmk_main,
)
from src.picokeyboard.code_generator.output_kmk_main import output_kmk_main
from src.picokeyboard.helper_files.user_interface import prompt_user

rel_wiring_filepath: str = "output/wiring_scheme.py"
kmk_main_rel_filepath: str = "keyboard_driver/main.py"
options = {
    1: "Get keyboard matrix",
    2: "Debug wiring",
    3: "Generate keyboard driver code",
    4: "Use keyboard",
}

from src.picokeyboard.helper_files.write_to_file import write_to_file

write_to_file(content="hello world", local_filepath="/home/a/hello.txt")

user_choice: int = prompt_user(options=options)
if user_choice == 1:
    # TODO: output the keyboard matrix to a file, and automatically load it
    # from that position once the driver is made.
    from src.picokeyboard.get_keyboard_matrix.generate_keyboard_matrix import (
        generate_keyboard_matrix,
    )

    generate_keyboard_matrix(filepath=rel_wiring_filepath)
elif user_choice == 2:
    # TODO: allow user to get the gpio pin on the pico, wire colour key and
    # pin nr on keyboard half connector for a specific key that malfunctions.
    from src.picokeyboard.debugging.debug_faulty_keys import (
        debug_faulty_keys,
    )

    debug_faulty_keys()
elif user_choice == 3:
    # TODO: output this locally and include it in src.
    keyboard_driver_main: str = generate_kmk_main()
    output_kmk_main(
        keyboard_driver_main=keyboard_driver_main,
        kmk_main_rel_filepath=kmk_main_rel_filepath,
    )
elif user_choice == 4:
    # If this code is not ran on the Pico, generate the Python code that
    # creates the KMK main.py file/driver for the keyboard.
    print(
        "TODO: copy the relevant files into the Pico, and verify the"
        " prerequisites are satisfied."
    )
else:
    raise SystemError("Please try again and enter a valid choice.")

# except ImportError:
#     pass  # ignore the error
