# multitask.py

import time
import threading

def Toothbrush():
    for i in range(10):
        print(f"{i} แปรฟังอยู่โว้ย......")

def Shower():
    for i in range(10):
        print(f"{i} กำลังอาบน้ำ...")

start = time.time() # จำเวลาเริ่มต้น

Toothbrush()
Shower()

end = time.time()
print('All Time: ', end - start)