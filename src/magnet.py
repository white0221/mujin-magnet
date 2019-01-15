from time import sleep
from threading import Thread
import RPi.GPIO as GPIO

pin = 17

# 扉が空いているかどうかを示す値
OPEN_FLAG = 1
CLOSE_FLAG = 0

#出力ピン18　BCMで指定
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# (注)実際にはこんな状態の変化はしません
# 　  デモバージョンです
class Magnet():
    def __init__(self):
       self.state = 0


    def get_state(self):
        if GPIO.input(pin) == GPIO.LOW:
            self.state = CLOSE_FLAG
        else:
            self.state = OPEN_FLAG
        return self.state


