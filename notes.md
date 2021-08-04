# Goldtouch_keyboard_driver
Creates Ubuntu driver for usb connection of bluetooth keyboard.

### Install Wireshark
Source: https://linuxhint.com/install_wireshark_ubuntu/
```
yes | sudo apt install wireshark
```
then chose yes when manually prompted.
````
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
Enter <yes> when prompted.

### Do at every reboot:
Source: https://askubuntu.com/questions/1114867/operation-not-permitted-when-trying-to-modprobe-xpad
Optional: Disable secure boot:
````
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


