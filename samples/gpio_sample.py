from time import sleep
import RPi.GPIO as GPIO

pin =17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while(1):
 print(GPIO.input(pin))

