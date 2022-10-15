from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for x in range(10):
            print("Hello \n")
            sleep(1)
class Hi(Thread):
    def run(self):
        for x in range(10):
            print("Hi \n")
            sleep(1)
t1=Hello()
t2=Hi()

t1.start()
t2.start()

t1.join()
t2.join()

print("PROCESS COMPLETED!")
