import multiprocessing
from time import sleep
def square_it(nums):
    for n in nums:
        print('Square: ', n**2)
        sleep(1)
def cube_it(nums):
    for n in nums:
        print('Cube: ', n ** 3)
        sleep(1)
if __name__=='__main__':
    data=[2,5,7,9,11]
    p1=multiprocessing.Process(target=square_it,args=(data,))
    p2=multiprocessing.Process(target=cube_it, args=(data,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("MULTIPROCESSING - COMPLETED!")