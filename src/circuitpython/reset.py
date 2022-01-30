import time
import board
import digitalio

out = digitalio.DigitalInOut(board.GP0)
out.direction = digitalio.Direction.OUTPUT
out.value = 1
out = None

out = digitalio.DigitalInOut(board.GP0)
out.direction = digitalio.Direction.OUTPUT
out.value = 1

btn_record = digitalio.DigitalInOut(board.GP16)
btn_record.direction = digitalio.Direction.INPUT
btn_record.pull = digitalio.Pull.DOWN

btn_stop = digitalio.DigitalInOut(board.GP17)
btn_stop.direction = digitalio.Direction.INPUT
btn_stop.pull = digitalio.Pull.DOWN

while True:
    if btn_record.value:
        # keyboard.press(Keycode.R)
        time.sleep(0.1)
        # keyboard.release(Keycode.R)
        print("0,16")
    if btn_stop.value:
        # keyboard.press(Keycode.SPACE)
        time.sleep(0.1)
        print("0,17")
        # keyboard.release(Keycode.SPACE)
    time.sleep(0.1)
