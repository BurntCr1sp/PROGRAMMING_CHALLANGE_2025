# SafeSleepClear.py

import time
import sys
import os
import select

def safe_sleep_clear(seconds=1):
    time.sleep(seconds)
    while select.select([sys.stdin], [], [], 0)[0]:
        sys.stdin.read(1)
    os.system('cls' if os.name == 'nt' else 'clear')
