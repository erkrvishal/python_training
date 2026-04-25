# import _thread
# import time

# def print_time(threadName, delay):
#     count = 0
#     while count <5:
#         time.sleep(delay)
#         count += 1
#         print(f"{threadName} {time.ctime(time.time())}")

# try:
#    _thread.start_new_thread(print_time, ("Thread-1", 10,))
#    _thread.start_new_thread(print_time, ("Thread-2", 5,))
# except Exception as error:
#    print(error)

# while 1:
#    pass

import threading
import time

exitFlag = 0

class myThread(threading.Thread):

    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print(f"Starting {self.name}")
        print_time(self.name, self.counter, 5)
        print(f"Exiting {self.name}")

def print_time(threadName, delay, count):
    while count:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print(f"{threadName} {time.ctime(time.time())}")
        count -= 1

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting the main thread")
