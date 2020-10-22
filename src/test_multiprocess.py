# https://pymotw.com/2/multiprocessing/basics.html

import multiprocessing
import time


def slow_worker():
    while True:
        print('Cycle')
        time.sleep(1)


if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print('BEFORE:', p, p.is_alive())

    p.start()
    print('DURING:', p, p.is_alive())

    time.sleep(5)
    p.terminate()
    print('TERMINATED:', p, p.is_alive())
    time.sleep(5)
    p.join()
    print('JOINED:', p, p.is_alive())
    time.sleep(5)
    print('main exited')