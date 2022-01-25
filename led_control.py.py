# Import GPIO And Time

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

try:
    while True:
        GPIO.output(11,True)
        time.sleep(.5)
        GPIO.output(11,False)
        time.sleep(.5)

finally:
    GPIO.cleanup()
