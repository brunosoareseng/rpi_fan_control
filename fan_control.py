import RPi.GPIO as GPIO

FAN_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

fan = GPIO.PWM(FAN_PIN, 100)

fan.start(30)