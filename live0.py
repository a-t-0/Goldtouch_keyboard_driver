# sudo su
# sudo apt install python3
# python3 live0.py
import pyshark


def print_packet_summary(pkt):
    print("    ", str(pkt)[:120])


# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries --------------------")
capture = pyshark.LiveCapture(interface='usbmon0')
capture.sniff(packet_count=50) # no packets detected
#capture.sniff(timeout=5)


# print capture to file:
def print_capture_to_file(capture):
    f = open("packets.txt", "a")
    for packet in capture:
        f.write(str(packet))
        f.write('\n\n')
    f.close()

print_capture_to_file(capture)