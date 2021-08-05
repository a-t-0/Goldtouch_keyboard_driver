# Source: https://stackoverflow.com/questions/59544706/how-can-i-save-a-filtered-pyshark-filecapture-to-a-new-pcap-file

# sudo su
# sudo apt install python3
# python3 live0.py
import pyshark
import os

# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries --------------------")
capture = pyshark.LiveCapture(interface="usbmon0", output_file="output.pcap")
capture.sniff(packet_count=50)  # no packets detected
# capture.sniff(timeout=5)


# Source: https://github.com/mzombor/Python-programs/blob/5efee9fe90a21ab20b1a10dcc95e2618dfedf1f8/CTF-scripts/crack2.py
# go over all the packets
for n in capture:
    try:
        # turn data into integer
        data = n[1].usb_capdata.split(":")
        print(data)
    except:
        pass
exit()


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
