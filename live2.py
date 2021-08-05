# Source: https://www.programcreek.com/python/example/92561/pyshark.LiveCapture
# sudo su
# sudo apt install python3
# python3 live0.py
import pyshark

def capture_on_interface(interface, name, timeout=60):
    """
    :param interface: The name of the interface on which to capture traffic
    :param name: The name of the capture file
    :param timeout: A limit in seconds specifying how long to capture traffic
    """

    if timeout < 15:
        logger.error("Timeout must be over 15 seconds.")
        return
    if not sys.warnoptions:
        warnings.simplefilter("ignore")
    start = time.time()
    widgets = [
        progressbar.Bar(marker=progressbar.RotatingMarker()),
        ' ',
        progressbar.FormatLabel('Packets Captured: %(value)d'),
        ' ',
        progressbar.Timer(),
    ]
    progress = progressbar.ProgressBar(widgets=widgets)
    capture = pyshark.LiveCapture(interface=interface, output_file=os.path.join('tmp', name))
    pcap_size = 0
    for i, packet in enumerate(capture.sniff_continuously()):
        progress.update(i)
        if os.path.getsize(os.path.join('tmp', name)) != pcap_size:
            pcap_size = os.path.getsize(os.path.join('tmp', name))
        if not isinstance(packet, pyshark.packet.packet.Packet):
            continue
        if time.time() - start > timeout:
            break
        if pcap_size > const.PT_MAX_BYTES:
            break
    capture.clear()
    capture.close()
    return pcap_size 

capture_on_interface('usbmon0', 'output_file', timeout=3):