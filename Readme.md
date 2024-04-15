# Creating/Modding your own Keyboard with a Raspberry Pico

This repository lets you use your Raspberri Pico as a keyboard. It helps you
get the wiring sceme after you wired your keyboard, and then writes the
code needed to use your Pico as a keyboard, using that sceme. It has a
separate debugging tool to show you which wire(s) have a bad connection if some
keys don't work.

- [Here](/Entertainment.md) is some entertainment story on why I created this.
- [Here](/Structure.md) is the structure of this repository.

To use this to build your own keyboard:

1. Install [the prerequisites](prerequisites/installation).
1. [Wire it](before-you-get-to-wiring).
1. [Run code to store wiring sceme file into repository](todo).
1. [Generate the code](todo) that you can use to use the keyboard, based on the
   generated wiring sceme file.
1. [Use the code to run the keyboard.](todo)

## 1. Prerequisites/Installation

1. Run:

```
sudo apt update
sudo apt install thonny
sudo snap install micropython

user=$(whoami)
echo "$user"
sudo usermod -a -G dialout $user
sudo reboot now
```

2. **In the bottom right of Thonny**, it may say: `Python 3.xx`, and you should
   click on it and then select:

```
MicroPython (Raspberry Pi Pico)
```

## 2. Wiring

For detailed wiring see [here](/Wiring.md).

## 3. Generate Wiring Sceme

This section is also moved into the [Wiring.md](/Wiring.md)

## 4. Generating the code to use the keyboard

TODO: ensure the user can generate the wiring sceme using the
`--generate-wiring` or `-gw` sceme.

## 5. Using the keyboard

open `thonny` by typing it in the CLI, then press `ctrl+o` and select the circuitPython device in the dialog
box. If it does not show that box, you have not selected the `MicroPython` in the bottom right of Thonnny,
and you should still do that. Then open `mwe0.py` and run it.

## TODO

- Make the driver start at boot.
- Add pictures to story.
