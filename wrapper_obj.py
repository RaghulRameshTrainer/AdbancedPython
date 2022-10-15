import inspect
def decorator(cls):     #3  cls=MyClass
    class Wrapper:             #5
        def __init__(self,x):   #6  x='Python'
            self.x=cls(x)       #7   MyClass('Python')

        def call_func(self):   #12
            return self.x.name  #13
    return Wrapper       #4

@decorator      #2
class MyClass:             #8
    def __init__(self,y):   #9
        self.name=y        #10
        print("METHODS ARE:", inspect.getmembers(MyClass))
    def abc(self):
        print("ABC")
    def xyz(self):
        print("XYZ")
mc=MyClass('Python')       # 1
print(mc.call_func())      #11