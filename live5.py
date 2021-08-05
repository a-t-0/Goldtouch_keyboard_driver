# Source: https://stackoverflow.com/questions/59544706/how-can-i-save-a-filtered-pyshark-filecapture-to-a-new-pcap-file

# sudo su
# sudo apt install python3
# python3 live5.py
import pyshark

# Get keystrokes
print("\n----- Capturing keystrokes from usbmon0 --------------------")
capture = pyshark.LiveCapture(interface="usbmon0", output_file="output.pcap")

# Source: https://www.programcreek.com/python/example/92561/pyshark.LiveCapture
for i, packet in enumerate(capture.sniff_continuously()):
    try:
        data = packet[1].usb_capdata.split(":")
        print(data)
    except:
        pass
capture.clear()
capture.close()
print(f"DONE")
