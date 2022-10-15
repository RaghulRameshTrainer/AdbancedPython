'''
Decorators is a function that accept another function as a argument
It has an inner function which collect the values passed to the called function
'''
import time

def calc_time(fn):
    def wrapper(*args, **kwargs):
        start=time.time()
        res=fn(*args,**kwargs)
        end=time.time()
        print(fn.__name__ + " took "+ str((end-start)*1000) + " milli seconds")
        return res
    return wrapper


@calc_time
def calc_square(nums):
    result=[]
    for n in nums:
        result.append(n**2)
    return result

@calc_time
def calc_cube(nums):
    result=[]
    for n in nums:
        result.append(n**3)
    return result

x=list(range(1,10000001))
# calc_square(x)
# calc_cube(x)

def check_value(fn):
    def inner(*args,**kwargs):
        if kwargs["num2"]==0:
            try:
                raise ValueError("Can't divide by zero")
            except ValueError as e:
                print("ERROR:",e)
        else:
            res=fn(*args,**kwargs)
            return res
    return inner

@check_value
def divide(**n):
    return n["num1"]/n["num2"]

print(divide(num1=10,num2=5))
divide(num1=10,num2=0)