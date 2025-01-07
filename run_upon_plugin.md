# Using wifi to run keyboard from terminal

## A. Identify Keyboard USB port.
0. Connect your pico through usb.
1. Get the port on which it runs with:

```sh
ls /dev/ttyACM* /dev/ttyUSB*
```

Yielding (for me):

```txt
ls: cannot access '/dev/ttyUSB*': No such file or directory
 /dev/ttyACM0
```

So it is at port: `/dev/ttyACM0`
2\. Install pip package to connect to the wireless Pico.

```sh
pip install mpremote
```

3. Connect to the wireless pico:

```sh
mpremote connect /dev/ttyACM0 run /media/a/CIRCUITPY/main.py
```

## B. Create script to run Pico keyboard.

0. Put this filecontent at `/home/a/run_pico_keyboard.sh`:

```sh
#!/bin/bash
echo "$(date '+%Y-%m-%d %H:%M:%S') Keyboard running script is started." > /home/a/git/hello.md

# Wait until CIRCUITPY is mounted
while [ ! -d "/media/a/CIRCUITPY" ]; do
    sleep 1
    echo "$(date '+%Y-%m-%d %H:%M:%S') Waiting for mount." >> /home/a/git/hello.md
done

{
    mpremote connect /dev/ttyACM0 run /media/a/CIRCUITPY/main.py >> /home/a/git/hello.md 2>&1
} || true
echo "$(date '+%Y-%m-%d %H:%M:%S') Done starting keyboard." >> /home/a/git/hello.md
```
``
## C. Ensure the Pico keyboard script runs upon plugin

Source: https://stackoverflow.com/questions/18463755/linux-start-daemon-on-connected-usb-serial-dongle
0. Create a rule that connects the keyboard usb port with the service to run the script:
```sh
sudo nano /etc/udev/rules.d/95-serialdaemon.rules
KERNEL=="ttyACM0", TAG+="systemd", ENV{SYSTEMD_WANTS}="serialdaemon.service"
```

1. Create a service that executes the rule/pico run script upon plugging in the keyboard:

```sh
sudo nano /lib/systemd/system/serialdaemon.service
```
With content:
```
[Unit]
Description=USB Pico Keyboard
After=remote-fs.target
After=syslog.target

[Service]
ExecStart=/home/a/run_pico_keyboard.sh
```
2. Then restart the service with:

```sh
sudo systemctl daemon-reload
sudo systemctl start serialdaemon.service
```
3. REBOOT YOUR PC with:
```sh
sudo reboot
```


## D. Debugging
```sh
journalctl -u serialdaemon.service -f
```

## E. Remove systemd
```sh
sudo systemctl stop /etc/systemd/system/run_pico_keyboard.service
sudo systemctl disable /etc/systemd/system/run_pico_keyboard.service
sudo rm /etc/systemd/system//etc/systemd/system/run_pico_keyboard.service.service
sudo systemctl daemon-reload
sudo systemctl reset-failed
```
