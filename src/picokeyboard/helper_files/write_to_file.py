import os


def write_to_file(*, content: str, local_filepath: str) -> None:
    # Open the file in write mode
    with open(f"{local_filepath}", "w") as file:
        file.write(content)


def assert_file_exists(*, file_path: str) -> None:
    """Checks if a file exists at the specified path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    file_exists = os.path.isfile(file_path)
    assert file_exists(file_path=file_path), f"File does not exist:{file_path}"


def file_exists(*, file_path: str) -> bool:
    """Checks if a file exists at the specified path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)
