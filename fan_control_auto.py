#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

FAN_PIN = 14
WAIT_TIME = 2
FAN_MIN = 20
PWM_FREQ = 30

tempSteps = list(range(55, 70))
speedSteps = list(range(0, 100))

hyst = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(0)

i = 0
cpuTemp = 0
fanSpeed = 0
cpuTempOld = 0
fanSpeedOld = 0

try:
    while 1:
        cpuTempFile = open("/sys/class/thermal/thermal_zone0/temp", "r")
        cpuTemp = float(cpuTempFile.read()) / 1000
        cpuTempFile.close()

        if abs(cpuTemp - cpuTempOld) > hyst:
            if cpuTemp < tempSteps[0]:
                fanSpeed = speedSteps[0]
            elif cpuTemp >= tempSteps[len(tempSteps) - 1]:
                fanSpeed = speedSteps[len(speedSteps) - 1]
            else:
                for i in range(0, len(tempSteps) - 1):
                    if (cpuTemp >= tempSteps[i]) and (cpuTemp < tempSteps[i + 1]):
                        fanSpeed = speedSteps[int(round(len(speedSteps) * i / len(tempSteps)))]
            if fanSpeed != fanSpeedOld:
                if fanSpeed >= FAN_MIN:
                    fan.ChangeDutyCycle(fanSpeed)
                else:
                    fan.ChangeDutyCycle(0)
                fanSpeedOld = fanSpeed
            cpuTempOld = cpuTemp

        time.sleep(WAIT_TIME)


except KeyboardInterrupt:
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()
