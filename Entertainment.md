# Entertainment

Hi, I incorrectly assumed the micro-usb port on the keyboard could be used to
connect the keyboard to the pc to type using the USB connection, when I
purchased it. Even though on the website the micro-USB connection is only for
charging. To learn from my mistakes, I wrote them down explicitly.

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
  all your keystrokes. [Excelent visual explanation](https://pcbheaven.com/wikipages/How_Key_Matrices_Works/)
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

Then I wrote the code that writes the code that contains the KMK keyboard
driver. Basically, KMK does all the heavy work and converts your Pico signals
into actual keypresses, and this code just creates the matrix that maps the
GPIO pin connections to the right keys based on your wiring. Then I found out
that I made a mistake in the wiring. All keys worked, but some rows (corresponding
to Pico GPIO pins 16 and 17) were also columns, and KMK does not accept that.
I also noticed that rows 6 and 7 functioned as columns. So I switched the two
wires into the left-hand side coming from Pico GPIO pins 16,17 with those
coming from the Pico GPIO pins 6,7 (at the LHS back side of the keyboard), and
updated the hardcoded wiring data accordingly.

Then I learned that I had to put all the keys of the matrix into a list, and
not into a list of lists with one list per row. You can have multiple key
matrices, for example to switch the keyboard behaviour if you press the FN key
but I did not yet do that. Also, it is important to specify the DIODE
orientation. For the Goldtouch keyboard it had to be:
`keyboard.diode_orientation = DiodeOrientation.COL2ROW`. I wrote these last
two paragraphs on the Goldtouch wireless foldable keyboard over USB with the
Pico!
