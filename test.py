import Encoder
import time
import RPi.GPIO as GPIO

PIN_UP = 20
PIN_DOWN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_UP, GPIO.OUT)
GPIO.setup(PIN_DOWN, GPIO.OUT)

if __name__ == "__main__":
    while (1):
        GPIO.output(PIN_UP,0)
        GPIO.output(PIN_DOWN,0)
        time.sleep(2)
        GPIO.output(PIN_UP,1)
        GPIO.output(PIN_DOWN,1)
        