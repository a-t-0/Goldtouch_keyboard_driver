# Repo Structure



0. First generate the code for your Pico keyboard using the code in this repository.
1. Plug in your Pico (or Pico W).
2. Ensure your raspberry Pico shows up as a drive on your pc.
3. "Flash" Circuit Python `uf2` to your Pico (or the [wireless variant](https://circuitpython.org/board/raspberry_pi_pico_w/) for your Pico W), by dragging that `uf2` file into the drive/folder of your Pico on your pc. Wait 2 minutes. The Pico should disconnect and reconnect as "CIRCUITPY` under "devices" in your file explorer.
4. 

3. copy the (generated) *content* of the  `keyboard_driver` folder of this repository into the root of your Pico (USB) drive. So the root of your Pico (USB) device should contain the `main.py` file.

4. Open Thonny. It should say CircuitPython (generic) in the bottom right and it should recognise your Pico.
Then open `thonny` then, inside `thonny`, open `src/picokeyboard/__main__.py` and run it by pressing the green run button. 


## Generating the code for your Pico keyboard (wiring)
 - The main code of this repo generates the code for the keyboard driver.
 - The main code of this repo runs on your Pico using MicroPython
 - The code for the keyboard driver runs on your Pico using CircuitPython
To select MicroPython/CircuitPython, you get the `.uf2` file from:
 ### MicroPython .uf2 file
 Wireless: https://micropython.org/download/RPI_PICO_W/
 Non-Wireless: https://micropython.org/download/RPI_PICO/

 ### CircuitPython .uf2 file
 Wireless: https://circuitpython.org/board/raspberry_pi_pico_w/
 Non-Wireless: https://circuitpython.org/board/raspberry_pi_pico/


## Old instructions
Then copy the code that is printed into the terminal into the `keyboard_driver/main.py` file.
- `circuitpython`: Contains a `flash_nuke.uf2` to factory reset your Pico. Contains Circuit Python v8.2.9. To flash a `uf2` file to your pico, press the bootsel button, then plugin the USB pico into your pc, and release the bootsel button when the Pico USB drive pops up on your pc. Then drag the `uf2` file into the Pico USB drive. Then wait until the circuitPython Pico USB drive pops up on your pc.
- `keyboard_driver`: After you are done with the wiring, etc. You can use the keyboard as a keyboard. Copy the content of the `keyboard_driver` into the root of the circuitPython Pico USB drive. Run `main.py`.


Micropython device does not show up, instead you can open files in thonny by clicking: view>files

Adafruit_Blinka
