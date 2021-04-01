#!/usr/bin/python3
# -*-coding:gb2312-*-
# coding : utf-8
# @Time  : 2021/3/16 11:08
# @File  : python_thread.py

__author__ = 'yangyanqin'
import _thread, logging, threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


# def loop_0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end  loop0 at " + ctime())
#
#
# def loop_1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end  loop1 at " + ctime())
#
#
# def main():
#     logging.info("start all at " + ctime())
#     _thread.start_new_thread(loop_0,())
#     _thread.start_new_thread(loop_1,())
#     sleep(6)
#     logging.info("end all at " + ctime())

# _thread

#
# def loop(nloop, nsec, lock):
#     logging.info("start loop " + str(nloop) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop " + str(nloop) + " at " + ctime())
#     lock.release()
#
#
# def main():
#     logging.info("start all at " + ctime())
#     locks = []
#     nloops = range(len(loops))
#     for i in nloops:
#         lock = _thread.allocate_lock()  # ������
#         lock.acquire()  # ����
#         locks.append(lock)
#
#     # �������߳�
#     for i in nloops:
#         _thread.start_new_thread(loop, (i, loops[i], locks[i]))
#
#     for i in nloops:
#         while locks[i].locked(): pass#�ж��Ƿ����ϣ�������������˳����߳�
#
#     logging.info("end all at " + ctime())


# threading

def loop(nloop, nsec):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())

def main():
    logging.info("start all at " + ctime())
    nloops = range(len(loops))
    threads = []

    for i in nloops:
        lock = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(lock)

    # �������߳�
    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    logging.info("end all at " + ctime())


# �̳� Thread

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


# def loop(nloop, nsec):
#     logging.info("start loop " + str(nloop) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop " + str(nloop) + " at " + ctime())
#
#
# def main():
#     logging.info("start all at " + ctime())
#     nloops = range(len(loops))
#     threads = []
#
#     for i in nloops:
#         lock = MyThread(loop, (i, loops[i]), loop.__name__)
#         threads.append(lock)
#
#     # �������߳�
#     for i in nloops:
#         threads[i].start()
#
#     for i in nloops:
#         threads[i].join()
#
#     logging.info("end all at " + ctime())


# ԭ���������ݵĻ������
# ��/�ź���

if __name__ == '__main__':
    main()
