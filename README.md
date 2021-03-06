# Goldtouch_keyboard_driver
Creates Ubuntu driver for usb connection of bluetooth keyboard.


## TL;DR
This repo converts a `.pcapng` file into its original keystrokes. For example, you can record the data that flows between your computer and keyboard by recording your USB port traffic with Wireshark. You can store that data as a `abcd.pcapng` file (e.g. I pressed `abcd` during that recording). Next the `parse_pcapng.py` converts that `abcd.pcapng` file into its original keystrokes. Run it with:
```
python parse_pcapng.py
```
- [ ] Next, I aim to make sure the USB port data is directly and continuously streamed into this python file, instead of first having to record and save the stream into a file.


### Install Wireshark
Source: https://linuxhint.com/install_wireshark_ubuntu/
```
yes | sudo apt install wireshark
```
then chose yes when manually prompted.
```
sudo usermod -aG wireshark $(whoami)
sudo reboot now
```

### Identify USB keystrokes from Goldtouch Model No. SK-2770 Bluetooth keyboard
Source: https://wiki.wireshark.org/CaptureSetup/USB

```
groups $USER
```
The output should contain "wireshark", IF NOT then run:
```
sudo adduser $USER wireshark
```


After you have ensured you're in the wireshark group, make sure non-superusers can capture packets in wireshark:
```
sudo dpkg-reconfigure wireshark-common
```
Enter `<yes>` when prompted.

### Do at every reboot:
Source: https://askubuntu.com/questions/1114867/operation-not-permitted-when-trying-to-modprobe-xpad
Optional: Disable secure boot:
```
sudo apt-get install mokutil
mokutil --sb-state
sudo mokutil --disable-validation
```

Then start modprobe
```
sudo setfacl -m u:$USER:r /dev/usbmon*
modprobe usbmon
```
If that says:
```
modprobe: ERROR: could not insert 'usbmon': Operation not permitted
```
Then run:
```
sudo modprobe usbmon
```
Start wireshark (if you ran `sudo modprobe usbmon` then start wireshark with sudo from terminal with: `sudo wireshark`).

### Record a usb input and inspect it later with wireshark
Record using another program: https://www.youtube.com/watch?v=0MC-D_oNzbk
Record directly in Wireshark: https://www.youtube.com/watch?v=cCXW9tSgfiQ
0. Remove all usb devices. 
1. Then in the 3/listed usb devices select the first one, e.g. `usbmon0` for the bottom left gate (on the Dell inspiron).
2. Click start recording, or double click the `usbmon0`.
3. Type `aaaaba`.
4. That generates a big list of data at each keypress.
5. Press stop recording.
6. Save the file as `aaaaba`.
7. Then search for:
Source: 1.7.1 (this represents your keyboard device id).
Destination: host (this represents your pc).
Protocol: USB
Length=72
Info= URB_INTERRUPT in
8. Then look at the `Leftover Capture Data` which says:
```
0000050000000000
```
for keypress `b`, and `0000040000000000`  for keypress `a` etc.

### Repo to get stream of Leftover Capture Data and convert it to keystrokes
https://github.com/grnbeltwarrior/USB_Keyboard_Hex

```
yes | sudo apt install tshark
git clone https://github.com/grnbeltwarrior/USB_Keyboard_Hex.git
cd USB_Keyboard_Hex
```
Then make the previously recorded `aaaaaba.pcapng` files readable, 
```
chmod 777
```
copy them into this repository and extract the Leftover Capture Data:
```
tshark -r 'data3.pcap' -T fields -e usb.capdata > data3.txt
```
Then create a final file that is supposed to remove only the zeros, but actually removes all the data:
```
cat data3.txt | cut -d':' -f 3 | grep -v '00' > data3_final.txt
```
Then run the python file on that last file with:
```
python USB_Hex.py
```
To get the keys that were pressed.

### Other Python stream approach
Source: https://stackoverflow.com/questions/57848983/how-to-convert-a-pcap-into-hex-stream-using-tshark

### Wireshark Keyboard Filtering Description:
Source: https://blog.stayontarget.org/2019/03/decoding-mixed-case-usb-keystrokes-from.html
 The relevant packets I was looking for in the pcap were the "URB_INTERRUPT in" packets from the source keyboard, which can be isolated with the filter usb.transfer_type == 0x01.  Looking at the Leftover Capture Data, there will be a series of 8 bytes strung together.  That third byte is the Usage ID for the key pressed (note this is not the same code as the ASCII hex value for the letter)

With that, I could add the Leftover Capture Data as a column (by right-clicking on one of the entries, and selecting "Apply as Column") then File -> Export Packet Dissections -> As CSV, open the resulting file, cut the capture data column out and the double-quotes, and the first line that says "Leftover Capture Data"

or:
```
tshark -r usb_flag.pcapng -T fields -e usb.capdata | tr -d :
tshark -r aaaaaaaba.pcapng -T fields -e usb.capdata | tr -d :
```
