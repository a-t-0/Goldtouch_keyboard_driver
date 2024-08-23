# Wiring Instructions

Here are the instructions on how to wire your Pico with your own keyboard.

### Before you get to wiring:

- Ensure that your wiring Pico GPIO pins results into `8/n` rows that do not
  occur in the column GPIO pins. I do not exactly know how to design this, just
  try something, run the code and see if the rows and columns have no overlap.
  If they do, rewire until they don't.

## Check all keys work

Open a terminal, type `thonny`, in `thonny` open `__main__.py`, run it and say
`y` to the half you want to get.
This asks you to press the keys, then it scans all GPIO ports on the Raspberry
Pico, and determines which two GPIO pins connect which key on the keyboard.
Current wiring 

# Left
1Yellow
2orange
GND
3red
4brown
5white
6purple
GND
7blue
RUN
8green


## Right
9gray 
10green
?
11yellow
12orange 
13Red
14brown
?
15black
16white
Top yelllow, bottom orange
pastel.whte-green
?
red-white
purple-yellow
brown-red
black- purple
?
gren-blue
blue-brown
