# multitask.py

import time
import threading

def Toothbrush(brand):
    for i in range(10):
        print(f"{i} แปรฟังอยู่โว้ย......{brand}")
        time.sleep(0.3)

def Shower(soap, gel):
    for i in range(10):
        print(f"{i} กำลังอาบน้ำ...")
        time.sleep(1)


''' TODO Thread '''
task1 = threading.Thread(target=Toothbrush, args=('Hello',))
task2 = threading.Thread(target=Shower)



start = time.time() # จำเวลาเริ่มต้น

''' เรียกใช้งาน function '''
# Toothbrush()
# Shower()

''' เรียกใช้งาน Threading ในการแสดงผล '''
task1.start()
task2.start()
task1.join()
task2.join()

end = time.time() # จำเวลาสิ้นสุด
print('All Time: ', end - start)