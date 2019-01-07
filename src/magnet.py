from time import sleep
from threading import Thread
import pigpio


# 購入中の待機時間(商品選んでいる時間)
OPEN_INTERVAL = 10
# 購入後の待機時間(次の人が来るまでの時間)
CLOSE_INTERVAL = 20

# 扉が空いているかどうかを示す値
OPEN_FLAG = 1
CLOSE_FLAG = 0

pi = pigpio.pi()
if not pi.connected:
 exit()
#出力ピン番号
pi.set_mode(8, pigpio.INPUT)
#pi.set_pull_up_down(8, pigpio.PUD_UP)

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
            self.state = pi.read(8)
            sleep(3)
            #self.state = OPEN_FLAG
            #sleep(OPEN_INTERVAL)
            #self.state = CLOSE_FLAG
            #sleep(CLOSE_INTERVAL)

