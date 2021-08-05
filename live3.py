# Source: https://stackoverflow.com/questions/59544706/how-can-i-save-a-filtered-pyshark-filecapture-to-a-new-pcap-file

# sudo su
# sudo apt install python3
# python3 live0.py
import pyshark
import os
from pprint import pprint

def print_packet_summary(pkt):
    print("    ", str(pkt)[:120])


# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries --------------------")
#capture = pyshark.LiveCapture(interface='usbmon0', output_file='/home/name/Documents/keyboard/Goldtouch_keyboard_driver/output.pcap')
capture = pyshark.LiveCapture(interface='usbmon0', output_file='output.pcap')
capture.sniff(packet_count=50) # no packets detected
#capture.sniff(timeout=5)


# Source: https://github.com/hmatuschek/qdmr/blob/af5cf97e5cfd015ceb2cfeb616562ac5719edccc/doc/reveng/anytone/d878uv/extract.py
def isDataPacket(p):
  return ("host" == p.usb.src) and ("USB.CAPDATA" in p)

def getData(p):
  if not isDataPacket(p): 
    return None
  return binascii.a2b_hex(p["USB.CAPDATA_RAW"].value)


#pprint(dir(capture))
#exit()
for packet in capture:
    #print(packet.capdata)
    #pprint(dir(packet))
    #print(packet.usb.src) # the source data
    #print(packet.usb.src)
    #if ("USB.CAPDATA" in packet):
    #   print(packet)
    #print(getData(packet))
    
    # get capdata
    try:
        print(packet["USB.CAPDATA_RAW"])
    except:
        pass
    
    # get wireshark colums
    #pprint(dir(packet.usb))
    
    #
    print(packet.usb.field_names)
exit()

# print capture to file:
def print_capture_to_file(capture):
    f = open("packets.txt", "a")
    for packet in capture:
        f.write(str(packet))
        f.write('\n\n')
    f.close()

print_capture_to_file(capture)
os.system('chmod 777 output.pcap')
os.system('chmod 777 packets.txt')