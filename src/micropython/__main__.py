import os
from .Main import Main

print(f"Hi, I'll be Thonny code on the Raspberry Pico.")

main = Main()
dictionary = main.get_key_matrix("output/right_dictionary.txt")
main.get_list_of_used_connections(dictionary)
main.get_list_of_gpio_connections_on_fpc()
print(f"Done.")
