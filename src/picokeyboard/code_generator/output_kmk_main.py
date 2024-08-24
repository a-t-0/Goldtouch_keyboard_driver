"""Overwrites the content of the main.py file that functions as the keyboard
driver."""


def output_kmk_main(keyboard_driver_main:str,kmk_main_rel_filepath:str) -> None:
    """Overwrites the keyboard_driver/main.py file with the code that functions
    as the keyboard driver based on how it is wired. The hardcoded wiring is stored
    in hardcoded.hardcoded_wiring."""
    # Open the file with write mode ('w') and specify the encoding
    with open(kmk_main_rel_filepath, "w", encoding="utf-8") as file:
        # Write the string to the file 
        file.write(keyboard_driver_main)