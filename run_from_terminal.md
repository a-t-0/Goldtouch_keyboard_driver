# Using wifi to run keyboard from terminal
0. Connect your pico through usb.
1. Get the port on which it runs with:
```sh
ls /dev/ttyACM* /dev/ttyUSB*
```
Yielding (for me):
```txt
ls: cannot access '/dev/ttyUSB*': No such file or directory
 /dev/ttyACM0
```
So it is at port: `/dev/ttyACM0`
2. Install pip package to connect to the wireless Pico.
```sh
pip install mpremote
```
3. Connect to the wireless pico:
```sh
mpremote connect /dev/ttyACM0 run /media/a/CIRCUITPY/main.py 
```