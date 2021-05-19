# multitask.py

import time
import threading

def Toothbrush():
    for i in range(10):
        print(f"{i} แปรฟังอยู่โว้ย......")
        time.sleep(0.3)

def Shower():
    for i in range(10):
        print(f"{i} กำลังอาบน้ำ...")
        time.sleep(1)


''' TODO Thread '''
task1 = threading.Thread(target=Toothbrush)
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