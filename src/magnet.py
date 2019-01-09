from time import sleep
from threading import Thread
import RPi.GPIO as GPIO


# 購入中の待機時間(商品選んでいる時間)
OPEN_INTERVAL = 10
# 購入後の待機時間(次の人が来るまでの時間)
CLOSE_INTERVAL = 20

# 扉が空いているかどうかを示す値
OPEN_FLAG = 1
CLOSE_FLAG = 0

#出力ピン18　BCMで指定
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# (注)実際にはこんな状態の変化はしません
# 　  デモバージョンです
class Magnet():
    def __init__(self):
        self.state = 0
        # 別スレッドで開け閉めを変更
        Thread(target=self.changing_state).start()

    def get_state(self):
        return self.state

    def changing_state(self):
        while(True):
            if GPIO.input(18) == GPIO.LOW:
                self.state = 1
            else:
                self.state = 0
            sleep(3)
            #self.state = OPEN_FLAG
            #sleep(OPEN_INTERVAL)
            #self.state = CLOSE_FLAG
            #sleep(CLOSE_INTERVAL)

