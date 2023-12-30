## Instructions
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

7. In the bottom right of Thonny, it may say: `Python 3.xx`, and you should click on it and then select: 
```
MicroPython (Raspberry Pi Pico)
(or: CircuitPython)
```  


9. Install `RPi.gpio` in Thonny by using: `Tools>Manage Plug-ins>Search for:`
```
RPi.GPIO
```

## Determining wiring strategy
The righthand panel (with the arrow keys) has a flat connector, that is connected to `X` GPIO output pins.
0. The connection from the solder of the flat connector to the pin is verified for pins: 0 to 19.
This verification is done by verifying there is a connection between the solder and the GPIO pin.
a single solder may still be connected to multiple GPIO pinss if there is a soldering error.
1. 

## Wiring sceme right hand side
The right-hand side (with arrow keys) is connected to GPIO (left) pins:
0,1,2,3,4,5,6,7

The right-hand side (with arrow keys) is connected to GPIO (right) pins:
8,9,10,11,12,13,14,15

## Wiring sceme left hand side
The left-hand side (without arrow keys) is connected to GPIO (left) pins:
0,1,2,3,4,5,6,7

The right-hand side (with arrow keys) is connected to GPIO (right) pins:
16,18,19,20,21,22,26,27,
Not: 17,23,24,25,28

So use this to wire the gpio pins to the right and left hand side of the board.
Then store a map with:
gpio 0 green->left-side pin 0 from the left (seen from back).
gpio 0 yellow->right-side pin 5 from the left (seen from back).
gpio 1 red->left-side pin 2 from the left (seen from back).
gpio 1 purple->right-side pin 6 from the left (seen from back).
...
gpio 17 Ornage -> left side pin 16 from the left (seen from the back).

etc.

## Running get_right_mapping.py for RHS
For the right hand side one observes the outer two pins on the flat connector are unused. Furthermore, the mapping below, along with the wiring sceme can be used to identify which connection is malfunctioning if a button is not responsive:
Key-Pico GPIO pin matrix:
  F8: (4, 15)  F9: (3, 15)  F10: (3, 14)  F11: (2, 14)  F12: (0, 14)  SCROLL_LOCK: (1, 15)  INSERT: (0, 15)  DELETE: (2, 15)
  7: (7, 14)  8: (5, 14)  9: (4, 14)  0: (6, 14)  MINUS: (6, 15)  EQUAL: (5, 15)  BACKSPACE: (3, 9)  BSPC: (3, 9)
  Y: (7, 13)  U: (7, 8)  I: (5, 8)  O: (4, 8)  P: (6, 8)  LBRACKET: (6, 13)  RBRACKET: (5, 13)  BACKSLASH: (5, 12)
  H: (7, 12)  J: (7, 11)  K: (5, 11)  L: (4, 11)  SEMICOLON: (6, 12)  QUOTE: (6, 11)  ENTER: (2, 8)  ENT: (2, 8)
  N: (7, 9)  m: (7, 10)  COMMA: (5, 10)  DOT: (4, 10)  SLASH: (6, 9)  RIGHT_SHIFT: (2, 12)  UP: (4, 9)  PRINT_SCREEN: (0, 8)
  SPACE: (1, 8)  SPC: (1, 8)  RIGHT_ALT: (0, 11)  RIGHT_SUPER: (3, 13)  RIGHT_CONTROL: (1, 10)  LEFT: (1, 9)  DOWN: (2, 9)  RIGHT: (0, 9)
  
### Wiring details RHS
As seen from back, with the flat connector at the bottom, GPIO pins on top, from left to right on the chip.
<GPIO pin nr on pico> - wire colour - <GPIO pin nr on keyboard RHS>
0-brown-2
1-blue-3
2-purple-4
3-red-5
4-yellow-6
5-white-7
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

(Skipping 0,1 18,19 on the flat connector)

## Running get_right_mappingV2 for LHS
For the left hand side one can see:
matrix
  ESCAPE: (3, 13)  F1: (7, 14)  F2: (8, 14)  F3: (4, 8)  F4: (11, 14)  F5: (12, 15)  F6: (6, 14)  F7: (11, 15)
  HOME: (5, 6)  GRAVE: (13, 14)  1: (5, 13)  2: (5, 7)  3: (5, 8)  4: (5, 10)  5: (10, 14)  6: (4, 10)
  PGUP: (5, 12)  TAB: (4, 13)  TAB: (4, 13)  Q: (13, 15)  W: (4, 7)  E: (8, 15)  R: (10, 15)  T: (2, 7)
  PGDOWN: (5, 11)  CAPS_LOCK: (7, 15)  CAPSLOCK: (7, 15)  A: (1, 13)  S: (3, 7)  D: (1, 8)  F: (1, 10)  G: (12, 14)
  END: (6, 15)  LEFT_SHIFT: (4, 9)  LSHIFT: (4, 9)  Z: (0, 13)  X: (0, 7)  C: (0, 8)  V: (0, 10)  B: (3, 8)
  ASTERISK: (5, 9)  LEFT_CONTROL: (1, 6)  LCTRL: (1, 6)  LEFT_SUPER: (3, 12)  LEFT_ALT: (0, 11)  SPACE: (9, 15)  SPC: (9, 15)  SPACE: (9, 15)

### Wiring details LHS
As seen from front of the keyboard, with the flat connector at the bottom, GPIO pins on top, from left to right on the chip.
Note there are double connections at GPIO pins 0 to 7, the LHS uses the top row of these wires.
<GPIO pin nr on pico> - wire colour - <GPIO pin nr on keyboard LHS>

0-blue-5
1-green-4
2-black-6
3-brown-7
4-purple-3
5-red-2
6-white-16
7-yellow-17
than from top left to bottom left on pico:
16-yellow-8
17-orange-9
18-red-10
19-brown-11
20-white-15
21-purple-14
22-blue-13
26-green-12

Skip pins 0,1,18,19

## Running for LHS
  ESCAPE: (0, 19)  F1: (7, 26)  F2: (3, 7)  F3: (3, 20)  F4: (4, 7)  F5: (1, 6)  F6: (7, 22)  F7: (4, 6)
  HOME: (21, 22)  GRAVE: (0, 7)  1: (0, 21)  2: (21, 26)  3: (3, 21)  4: (5, 21)  5: (5, 7)  6: (5, 20)
  PGUP: (1, 21)  TAB: (0, 20)  TAB: (0, 20)  Q: (0, 6)  W: (20, 26)  E: (3, 6)  R: (5, 6)  T: (17, 26)
  PGDOWN: (4, 21)  CAPS_LOCK: (6, 26)  CAPSLOCK: (6, 26)  A: (0, 18)  S: (19, 26)  D: (3, 18)  F: (5, 18)  G: (1, 7)
  END: (6, 22)  LEFT_SHIFT: (2, 20)  LSHIFT: (2, 20)  Z: (0, 16)  X: (16, 26)  C: (3, 16)  V: (5, 16)  B: (3, 19)
  ASTERISK: (2, 21)  LEFT_CONTROL: (18, 22)  LCTRL: (18, 22)  LEFT_SUPER: (1, 19)  LEFT_ALT: (4, 16)  SPACE: (2, 6)  SPC: (2, 6)  SPACE: (2, 6)
>>> 



## TODO:
- create separate function/file that takes in the wiring and key-pin relations to tell the user which wire is not connected properly if a keyboard button does not work.
- rewrite get_mapping_V2 such that it also automatically outputs which wire is not connected properly, if there is any wire not connected properly.
- Create a dictionary output method for the keyboard matrices. (Prompt user for y/n to ask if user wants to export)
- Give user option to specify left/right keyboard half.
- Write a driver for the keyboard.
- Make the driver start at boot.
- Clean up the repo.
- Write a brief story, include pictures, post.
