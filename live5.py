# Source: https://stackoverflow.com/questions/59544706/how-can-i-save-a-filtered-pyshark-filecapture-to-a-new-pcap-file

# sudo su
# sudo apt install python3
# python3 live0.py
import pyshark
import os

# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries --------------------")
capture = pyshark.LiveCapture(interface='usbmon0', output_file='output.pcap')
#capture.sniff(packet_count=50) # no packets detected
#capture.sniff(timeout=5)

# Source: https://www.programcreek.com/python/example/92561/pyshark.LiveCapture
 
for i, packet in enumerate(capture.sniff_continuously()):
    #if os.path.getsize(os.path.join('tmp', name)) != pcap_size:
    #    pcap_size = os.path.getsize(os.path.join('tmp', name))
    #if not isinstance(packet, pyshark.packet.packet.Packet):
    #    continue
    try:
        data= packet[1].usb_capdata.split(":")
        print(data)
    except:
        pass
capture.clear()
capture.close()
print(f'DONE')
exit()