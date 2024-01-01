def export_connected_pins_per_key(
    abs_output_dir, filename, connected_pins_per_key
):
    filepath = f"{abs_output_dir}/{filename}"
    print(f"filepath={filepath}")
    write_dictionary_to_file(
        f"{abs_output_dir}/{filename}", connected_pins_per_key
    )


def write_dictionary_to_file(abs_filepath, dictionary):
    import json

    with open(abs_filepath, "w") as convert_file:
        convert_file.write(json.dumps(dictionary))


def write_to_file(abs_filepath, lines):
    f = open(abs_filepath, "w")
    for line in lines:
        f.write(line)
    f.close()
