# Creating/Modding your own Keyboard with a Raspberry Pico

This repository lets you use your Raspberri Pico as a keyboard. It helps you
get the wiring scheme after you wired your keyboard, and then writes the
code needed to use your Pico as a keyboard, using that scheme. It has a
separate debugging tool to show you which wire(s) have a bad connection if some
keys don't work.

- [Here](/Entertainment.md) is some entertainment story on why I created this.

## Terminology

- *OS* Operating System, like Windows, Ubuntu, and for the Pico, `CircuitPython` or MicroPython.
- *Flashing* your Pico (copy paste a `.uf2` file on the pico storage), once it is
  pasted, the Pico will reboot itself and install the software/Pico OS on it.
- *Thonny* a program to interact with your Pico.

## Context

This repo currently consists of 4 code modules:

1. keyboard matrix getter
1. keyboard wiring debugger
1. keyboard driver code generator
1. keyboard driver code
   And it uses redundant wiring information to help you debugging if anything goes
   sub-optimal. The wiring is stored:

In terms of wire objects that each consist of:

- GPIO pin numbers on the pico
- Pin number on the keyboard pin connector
- Wire colour

6. A keyboard matrix that is eventually used in the keyboard driver code.
   The `Wire` objects are used in the debugger to tell you:

```
The <yellow> wire
from Pico GPIO pin `<4>` to <left> hand keyboard half Pin nr `<7>` is not
connected properly.
```

This makes it a lot easier to determine which wire has gotten loose, even
though you could have also derived that information from the keyboard matrix.

## Flow

1. You install Thonny.
1. You *flash* CircuitPython onto your Pico.
1. You copy the code of this repo onto your Pico.
1. You tell this repo how you wired it (in the code of this repo).
1. You use this repo to generate the keyboard matrix for your keyboard by
   pressing each key when it asks you to, the code then stores the GPIO pin numbers
   that belong to that key, as a `keyboard matrix`.
1. You store that `keyboard matrix` in the code of this repo.
1. You generate the keyboard driver code.
1. You copy the keyboard driver code to your keyboard.
1. You use your keyboard by connecting it to your pc, opening `Thonny` and
   running the main code.

## Instructions

- 0\. Install Thonny on your pc with:

```sh
sudo apt update
sudo apt install thonny
sudo snap install micropython
```

- 1\. And give it the permissions it needs to recognize the Pico:

```sh
user=$(whoami)
echo "$user"
sudo usermod -a -G dialout $user
sudo reboot now
```

- 2\. Connect your Pico to the pc.

  - 2.1. If it shows up as a drive:

    - 2.1.1. format the Pico by flashing `.uf2` of CircuitPyhon on it.
      The code for the keyboard driver runs on your Pico using `CircuitPython`
      To select `CircuitPython`, you get the `.uf2` file from the overview below:

      - 2.1.1.1. `CircuitPython` .uf2 file

        Wireless: https://CircuitPython.org/board/raspberry_pi_pico_w/

        Non-Wireless: https://CircuitPython.org/board/raspberry_pi_pico/

      - 2.1.1.2. MicroPython .uf2 file

        Wireless: https://micropython.org/download/RPI_PICO_W/

        Non-Wireless: https://micropython.org/download/RPI_PICO/

      So copy the `CircuitPython` `.uf2` file to your Pico.

  - 2.2. If it does not show up as a drive, eiher it is broken, or you have MicroPyhon installed on it.

    - 2.2.1. If it has MicroPython installed on it, open the Pico in
      `Thonny`, press `View>Files`,and that will open up a tab split in half,
      with the upper half as a file explorer on your pc, and the lower half being
      the Pico storage. You can then "copy" your `.uf2` file into your MicroPython
      Pico using the "RMB>upload to /`option when you click on your`.uf2`file in the file explorer for your pc in the`file`view of thonny. Then wait a minute, the Pico will disconnect, flash the new`.uf2\` file (with `CircuitPython`), and
      reconnect (this time as a mountable USB drive).
    - 2.2.2. If it is broken, try to see if you can:
      - press the Bootsel button and plugging the Pico USB into the PC, followed by
        releasing the button to reset the Pico.
      - Connect the reset button to the ground (or something like that), to reset
        the Pico.
      - *flash* the "flash_files/non-wireless/flash_nuke.uf2\` file on it.

- 3\. Your Pico is now connected to your laptop, shows up as a drive, and has CircuitPython on it.

- 4\. Write down how you wired the Pico to the Keyboard by filling the parameters:

```py
hardcoded_lhs_wires
hardcoded_rhs_wires
```

in the `hardcoded_wiring.py` file. The specific instructions are in that file as a comment.

- 5\. Once the code knows how you wired it, it can verify which button is
  connected to which GPIO port on your pico, and create a keyboard matrix for
  you, that will be used by the keyboard driver. To generate this matrix, run:

  - 5.1. Copy the `src` dir and `boot.py` file of this repository into the root of the USB drive with
    CircuitPython. <TODO>

  - 5.2. Open the `src/picokeyboard/__main__.py` file in Thonny on the Pico, <TODO>

  - 5.4. Run the `__main__.py` file (with `F5`) and follow the instructions. <TODO>

  - 5.4.1. If you have a perfectly working keyboard:

    - 5.4.1.1. keyboard copy the output matrix of the left half and copy it into:
      `hardcoded_wiring.py` variable: `hardcoded_lhs` <TODO>
    - 5.4.1.2. then copy the output matrix of the right half into:
      `hardcoded_wiring.py` variable: `hardcoded_rhs`

  - 5.4.2. you  have some faulty connections.

    - 5.4.1.1. The output tells you which connections are bad, pick up
      some electricity meter, verify that those connections are bad,
      wiggle the wires and fix it. Then go back to step 4.4 (repeat till it
      works).

- 6\. Now that the wiring and keymapping are determined, you can

- 7\. Generate the Pico keyboard driver code, by setting:

```py
store_wiring = False
debug_wiring = False
create_keybaord_driver = True
install = False
use = False
```

- 8\. ANd run:

```sh
python -m src.picokeyboard.__main__
```

This outputs the updated keyboard driver to (the `main.py` file in) `/keyboard_driver`.

- 9\. delete the `src/` folder from the
  CircuitPython Pico, copy the generated *content* of the  `keyboard_driver` folder of this repository into the root of your Pico (USB) drive. So the *root* of your Pico (USB) device should contain the `main.py` file.

- 10\. Open Thonny. It should say CircuitPython (generic) in the bottom right and it should recognise your Pico.
  Then open `thonny` then, inside `thonny`, open `src/picokeyboard/__main__.py` and run it by pressing the green run button.

## Resetting

If you want to drop a flash nuke `.uf2` file on it but it says: not enough space even though you deleted everything form the drive, run:

```py
import microcontroller
microcontroller.on_next_reset(microcontroller.RunMode.UF2)
microcontroller.reset()
```

in the `thonny` shell on the python. That resets it and makes it eager to take in a `.uf2` file.

If you are in MicroPython (instead of CircuitPython), type:

```py
machine.bootloader()
```

(*without* typing `import machine` first).

## Enabling CircuitPython to write files to itself:

Create a `boot.py` at the root of the CircuitPython USB drive with content:

```py
import storage
storage.remount('/', readonly=False)
```

Then you can make the CircuitPython create files inside the CircuitPython USB drive with:

```
with open('/x.txt`, 'w') as f:
  f.write(b'abcdefg')
```
