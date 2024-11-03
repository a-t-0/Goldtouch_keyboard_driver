import os

from src.picokeyboard.code_generator.output_kmk_main import output_kmk_main
from src.picokeyboard.helper_files.write_to_file import (
    assert_file_exists,
    file_exists,
)


def assert_can_run(
    *,
    kmk_main_rel_filepath: str,
    kmk_rel_dir_path: str,
    keyboard_driver_main: str,
) -> None:
    """Checks if everything needed to run the code is available, and if not,
    tries to ensure it is, and if that fails, stops execution."""

    if not file_exists(file_path=kmk_main_rel_filepath):
        output_kmk_main(
            keyboard_driver_main_content=keyboard_driver_main,
            kmk_main_rel_filepath=kmk_main_rel_filepath,
        )
    assert_file_exists(file_path=kmk_main_rel_filepath)  # Superfluous.

    if not os.path.exists(kmk_rel_dir_path):
        raise NotImplementedError(
            "Please copy kmk dir to the root of this CircuitPython device."
        )
