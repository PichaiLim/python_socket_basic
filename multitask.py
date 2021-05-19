# multitask.py

import time
import threading

def Toothbrush():
    for i in range(10):
        print(f"{i} แปรฟังอยู่โว้ย......")

def Shower():
    for i in range(10):
        print(f"{i} กำลังอาบน้ำ...")

Toothbrush()
Shower()