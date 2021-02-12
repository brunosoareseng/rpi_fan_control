# Fan control in Rpi

## How to install

sudo mv fan_control_auto.py /usr/local/bin/

sudo chmod +x /user/local/bin/fan_control_auto.py

## Execute on boot

sudo mv fan_control_auto.sh /etc/init.d/

sudo chmod +x /etc/init.d/fan_control_auto.sh

sudo update-rc.d fan_control_auto.sh defaults

sudo /etc/init.d/fancontrol.sh start