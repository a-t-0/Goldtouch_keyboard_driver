# Source: https://stackoverflow.com/questions/59544706/how-can-i-save-a-filtered-pyshark-filecapture-to-a-new-pcap-file
# sudo su
# sudo apt install python3
# python3 live0.py
import pyshark
import os


def print_packet_summary(pkt):
    print("    ", str(pkt)[:120])


# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries --------------------")
# capture = pyshark.LiveCapture(interface='usbmon0', output_file='/home/name/Documents/keyboard/Goldtouch_keyboard_driver/output.pcap')
capture = pyshark.LiveCapture(interface="usbmon0", output_file="output.pcap")
capture.sniff(packet_count=5)  # no packets detected
# capture.sniff(timeout=5)


# print capture to file:
def print_capture_to_file(capture):
    f = open("packets.txt", "a")
    for packet in capture:
        f.write(str(packet))
        f.write("\n\n")
    f.close()


print_capture_to_file(capture)
os.system("chmod 777 output.pcap")
os.system("chmod 777 packets.txt")
