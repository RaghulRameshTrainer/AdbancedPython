from oops import Employee
from test import AnotherClass

class CallClass(Employee,AnotherClass):
    # def __init__(self,name):
    #     self.name=name.upper()
    def __add__(self,):
        return empobj.salary+another.amount

c=CallClass('Rajesh','Kumar',10000)
print(c.name)
e=Employee('Satya','Bala',20000)
a=AnotherClass('Saranya',30000)

print(c.__add__(e,a))
