#! /bin/sh

### BEGIN INIT INFO
# Provides:          fan_control_auto.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting fan_control_auto.py"
    /usr/local/bin/fan_control_auto.py &
    ;;
  stop)
    echo "Stopping fan_control_auto.py"
    pkill -f /usr/local/bin/fan_control_auto.py
    ;;
  *)
    echo "Usage: /etc/init.d/fan_control_auto.sh {start|stop}"
    exit 1
    ;;
esac