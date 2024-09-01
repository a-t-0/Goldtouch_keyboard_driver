def write_to_file(*, content: str, local_filepath: str) -> None:
    # Open the file in write mode
    with open(f"{local_filepath}", "w") as file:
        file.write(content)
