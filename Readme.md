# Converting Goldtouch bluetooth keyboard to USB

Hi, I incorrectly assumed the micro-usb port on the keyboard could be used to
connect the keyboard to the pc to type using the USB connection, when I
purchased it. Even though on the website the micro-USB connection is only for
charging.

## Issue

Then it happened that the bluetooth connection does not work well, and results
in hanging keys every now and then, this is particularly hindering when it is
the delete or enter button, e.g. when filling in webforms. According to the
support some steps can be taken to resolve the issue in 99% of the cases. No
substantiation is given for that number, and I was not able to apply the steps
to resolve the issue. I am a big fan of the ergonomics of the keyboard and the
feel. Hence, I converted it from bluetooth to USB using a Raspberry Pico.

## Entertainment - road to Pico

This section explains how I ended up doing this. I initially did not believe
that it would not be possible to not send the keystrokes over the micro-USB
port for the keyboard. I assumed it would be more expensive to buy a chip with
a micro-USB port for charging only, than to just softwarematically disable the
micro-USB keypress-send option. A bit like how modern cars have functionalities
like heated seats, that are softwarematically disabled to squeeze
consumers/maximise revenue. I assumed Goldtouch imagined it would be more hip
if people used their keyboards wirelessly, and hence disabled the future. At
the time, I did not look into the micro-USB port to determine whether it indeed
was charging only.

First I learned to use wireshark to capture the keystroke data. And it worked.
I plugged in the keyboard, and was able to recognise the keystrokes in, I
think, binary or hex format in some USB port on wireshark. So I wrote a code
that automatically captures the Goldtouch keystrokes. And I think I wrote a
code that converted that keystroke data into actual keypress events. However,
I did not write a code that starts wireshark in the background upon boot. Then
time-constraints regarding studies prevented me from finalising the project, so
I had to drop the project for a few months.

That summer, I picked up the project again, and I reformatted my pc a few
times, and lost the code I wrote. So I went back into Wireshark, and was not
able to detect the keystrokes. After a few days I realised, that at the time I
did this, the laptop had some internal bluetooth module, that I had to make
Ubuntu compatible, which I believe, at the time was hence mapped to some
internal USB port. So instead of actually having read out the data that went
over the micro-USB port, I read out the data that was sent over bluetooth. And
the bluetooth connection was causing the hanging-keys problem. I did not check
if my own wireshark "keyboard-driver" was able to overcome that problem.

So then I successfully applied the sunk cost fallacy and became more determined
to make it work. So I ordered a Raspberry Pico and some jumper wires, and 2
things that convert an flexible flat cable (FFC) into (GPIO) pins on which you
can connect the jumper wires, and some double sided tape. After installing the
Pico and thonny on my laptop and verifying I was able to detect a (jumper wire)
connection between two GPIO pins on the Pico, I tried to find out how the
keyboard was wired on the flexible flat cables.

It was not clear to me that the keys are mapped on a matrix, where the each row
and each column has a separate wired connection on the flexible flat cable. So
I did not understand how one can send the signals of 64 different keys over 19
wires. After someone explained that to me, I understood one could send the
signals of 64 cables over 8 rows, and 8 columns, yielding 16 wires. What your
keyboard (likely) does is:

- check if wire 0 and wire 8 are connected. If yes, ESC is pressed.
- check if wire 0 and wire 9 are connected. If yes, F1 is pressed etc.
  ..
- check if wire 1 and wire 8 are connected. If yes, TAB is pressed.
- check if wire 1 and wire 9 are connected. If yes, Q is pressed.
  etc.
  But then for the entire matrix, a few (hundred?) times per second, to catch
  all your keystrokes.
  Since the Raspberry Pico only has 24 GPIO pins, instead of 32, I was able to
  use the pins 0 to 7 twice, once for the rows on the left half of the
  keyboard, and once for the right half of the keyboard (each consisting of 64
  keys). Then the remaining pins 8 to 26 are used to determine which half, and
  which key is pressed. So I soldered u-bridge GPIO pins on GPIO positions 0
  to 7 on the Pico.

Then I connected the wires from GPIO pins:

```
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,26
```

to the FFC pins:

```
2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17
```

where the outer two pins, pins `0,1` and `18,19` were unused. Then I applied
tiewraps to hold the cables in place, and wrote software to detect which key
belonged to which GPIO port. Then I remounted the keyboard, and with full
excitement gave it a trie. And then all buttons worked except for one. The
bottom left control button. I started using it, thinking I could do without
that one button, as there was a ctrl button on the righ-hand side as well. I
was wrong, again. `Ctrl+C` and `Ctrl+V` are used a lot by me. I opened it up
again, pushed all the connectors into the pins, yet did not resolve the issue.
Furthermore, I did not write down the wiring color scheme I used, and did not
know which two pins on the FFC corresponded to which key press. Hence I did
not know which wire was having a bad connection. Time constraints prevented
from debugging the issue further, and the tiewraps made it difficult to
re-open the keyboard without pulling out more connections.

Recently, some projects were completed, granting me more time to make the
keyboard work. To apply better cable management, I wrote a basic kit to
fabric my own jumper wires of custom length. Furthermore I wrote down the
jumper wiring colour scheme. So I took out the original wires, re-wired it,
re-applied the tie-wraps, verified ALL keys work, remounted the keyboard,
verified all keys worked again. Folded it, opened it, verified the connections
hold.

Then I wrote some software that takes in the wiring scheme and automatically
tells you which wire is causing the issues if a key stops working. Then I wrote
a driver to start the keyboard driver at boot. I did not type this from the
modded Goldtouch keyboard.

## Prerequisites/Installation

1. Run:

```
user=$(whoami)
echo "$user"
sudo usermod -a -G dialout $user
sudo reboot now

pip3 install thonny

sudo apt update
sudo apt install snapd
sudo snap install micropython
```

2. In the bottom right of Thonny, it may say: `Python 3.xx`, and you should
   click on it and then select:

```
MicroPython (Raspberry Pi Pico)
```

(or for the `get_key_gpio_mapping.py`):

```
CircuitPython
```

3. Install `RPi.gpio` package/library in Thonny by using:

```
Tools>Manage Plug-ins>Search for:
```

```
RPi.GPIO
```

Then you have to probably restart thonny to enable it to use the recently
installed library.

## Check all keys work

Open a terminal, type `thonny`, in `thonny` open `__main__.py`, run it and say
`y` to the half you want to get.
This asks you to press the keys, then it scans all GPIO ports on the Raspberry
Pico, and determines which two GPIO pins connect which key on the keyboard.

### Key-Pico GPIO pin matrix RHS:

F8: (4, 15)  F9: (3, 15)  F10: (3, 14)  F11: (2, 14)  F12: (0, 14)  SCROLL_LOCK: (1, 15)  INSERT: (0, 15)  DELETE: (2, 15)

7: (7, 14)  8: (5, 14)  9: (4, 14)  0: (6, 14)  MINUS: (6, 15)  EQUAL: (5, 15)  BACKSPACE: (3, 9)  BSPC: (3, 9)

Y: (7, 13)  U: (7, 8)  I: (5, 8)  O: (4, 8)  P: (6, 8)  LBRACKET: (6, 13)  RBRACKET: (5, 13)  BACKSLASH: (5, 12)

H: (7, 12)  J: (7, 11)  K: (5, 11)  L: (4, 11)  SEMICOLON: (6, 12)  QUOTE: (6, 11)  ENTER: (2, 8)  ENT: (2, 8)

N: (7, 9)  m: (7, 10)  COMMA: (5, 10)  DOT: (4, 10)  SLASH: (6, 9)  RIGHT_SHIFT: (2, 12)  UP: (4, 9)  PRINT_SCREEN: (0, 8)

SPACE: (1, 8)  SPC: (1, 8)  RIGHT_ALT: (0, 11)  RIGHT_SUPER: (3, 13)  RIGHT_CONTROL: (1, 10)  LEFT: (1, 9)  DOWN: (2, 9)  RIGHT: (0, 9)

### Wiring details RHS

This describes how the right-hand side is wired.

- Skipping 0,1 18,19 on the flat connector because the outer 2 pins on each end of the flat connector on the back of the keyboard half are unused.
- As seen from back, with the flat connector at the bottom, GPIO pins on top, from left to right on the chip.

<GPIO pin nr on Pico> - wire colour - <GPIO pin nr on keyboard RHS>
0-brown-2
1-blue-3
2-purple-4
3-red-5
4-yellow-6
5-white-7# TODO: Create a dictionary output method for the keyboard matrices. (Prompt

# user for y/n to ask if user wants to export) and verify you can read

# it in again.

6-green-8
7-orange-9
8-white-10
9-black-11
10-brown-12
11-red-13
12-orange-14
13-yellow-15
14-green-16
15-gray-17

## Running get_key_gpio_mapping.py for LHS

For the left hand side one can see:
matrix
ESCAPE: (0, 19)  F1: (7, 26)  F2: (3, 7)  F3: (3, 20)  F4: (4, 7)  F5: (1, 6)  F6: (7, 22)  F7: (4, 6)

HOME: (21, 22)  GRAVE: (0, 7)  1: (0, 21)  2: (21, 26)  3: (3, 21)  4: (5, 21)  5: (5, 7)  6: (5, 20)

PGUP: (1, 21)  TAB: (0, 20)  TAB: (0, 20)  Q: (0, 6)  W: (20, 26)  E: (3, 6)  R: (5, 6)  T: (17, 26)

PGDOWN: (4, 21)  CAPS_LOCK: (6, 26)  CAPSLOCK: (6, 26)  A: (0, 18)  S: (19, 26)  D: (3, 18)  F: (5, 18)  G: (1, 7)

END: (6, 22)  LEFT_SHIFT: (2, 20)  LSHIFT: (2, 20)  Z: (0, 16)  X: (16, 26)  C: (3, 16)  V: (5, 16)  B: (3, 19)

FN: (2, 21)  LEFT_CONTROL: (18, 22)  LCTRL: (18, 22)  LEFT_SUPER: (1, 19)  LEFT_ALT: (4, 16)  SPACE: (2, 6)  SPC: (2, 6)  SPACE: (2, 6)

### Wiring details LHS

This describes how the left-hand side is wired.

- Skipping 0,1 18,19 on the flat connector because the outer 2 pins on each end of the flat connector on the back of the keyboard half are unused.
- As seen from front of the keyboard, with the flat connector at the bottom, GPIO pins on top, from left to right on the chip.
- Note there are double connections at GPIO pins 0 to 7, the LHS uses the top row of these wires.
  <GPIO pin nr on Pico> - wire colour - <GPIO pin nr on keyboard LHS>
  0-blue-5
  1-green-4
  2-black-6
  3-brown-7
  4-purple-3
  5-red-2
  6-white-16
  7-yellow-17
  than from top left to bottom left on Pico:
  16-yellow-8
  17-orange-9
  18-red-10
  19-brown-11
  20-white-15
  21-purple-14
  22-blue-13
  26-green-12

## TODO:

- Identify and switch the jumper wires leaving GPIO pin 6,7 with those leaving GPIO pin 16,17 (on the LHS side of the keyboard.). Then recreate the hardcoded wiring. Then recreate the kmk keyboard driver code, then run it to verify it works. (The issue is that the columns and rows have overlapping GPIO pins, which is not supported by KMK.)

- Make the driver start at boot.

- Add pictures to story.

## Rows and columns

Derived from hardcoded:
Left half:
Rows:\[0, 1, 2, 3, 4, 5, 6, 7, 16, 17\]
Cols:\[6, 7, 16, 17, 18, 19, 20, 21, 22, 26\]
Right half:
Rows:\[0, 1, 2, 3, 4, 5, 6, 7\]
Cols:\[8, 9, 10, 11, 12, 13, 14, 15\]

## Repo content description

- `src`: The Python source code that allows you to verify and debug your Pico keyboard wiring. Flash Circuit Python `uf2` to your Pico, then copy the `src` folder into the Pico (USB) drive. Then open `thonny` then, inside `thonny`, open `src/pythontemplate/__main__.py` and run it by pressing the green run button.
- `circuitpython`: Contains a `flash_nuke.uf2` to factory reset your Pico. Contains Circuit Python v8.2.9. To flash a `uf2` file to your pico, press the bootsel button, then plugin the USB pico into your pc, and release the bootsel button when the Pico USB drive pops up on your pc. Then drag the `uf2` file into the Pico USB drive. Then wait until the circuitPython Pico USB drive pops up on your pc.
- `keyboard_driver`: After you are done with the wiring, etc. You can use the keyboard as a keyboard. Copy the content of the `keyboard_driver` into the root of the circuitPython Pico USB drive. Run `main.py`.
