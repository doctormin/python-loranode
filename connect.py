from loranode import RN2483Controller
from loranode.rpyutils import set_debug_level, Level
import os
import time

set_debug_level(Level.DEBUG)

files = os.listdir("/dev")
file = list(filter(lambda x: "tty.usbmodem" in x, files))[0]
print("Connect to ", file)
lc = RN2483Controller(f"/dev/{file}")

lc.set_freq("868100000")
lc.set_cr("4/5")
lc.set_bw("125")
lc.set_sf("sf11")
lc.set_crc("on")
lc.set_prlen("8")

data = "aaaaaa"
while True:
    lc.send_p2p(data)
    time.sleep(2)
