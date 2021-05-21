import threading
from threading import Lock, Thread
import time
import os


def run(n):
    print('task', n)
    time.sleep(1)
    print('3s')
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=('t1',))
    t1.setDaemon(True)
    t2 = threading.Thread(target=run, args=('t2',))
    t2.setDaemon(True)

    t1.start()
    t1.join()
    t2.start()
    t2.join()

    print('end')
