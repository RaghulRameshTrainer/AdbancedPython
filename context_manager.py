# with open('tech.txt') as fo:
#     print(fo.read())
#
# print(fo.closed)
#
# fo=open('tech.txt')
# print(fo.read())
# fo.close()
# print(fo.closed)
"""
class MyClass():
    def __init__(self):
        print("Constructor called")

    def __enter__(self):
        print("enter method called")
        return self
    def sayHi(self):
        print("Hi Everyone!")

    def __exit__(self,x,y,z):
        print("exit method called")

with MyClass() as mc:
    print("My Statement")
    mc.sayHi()
"""

class ReadFile():
    def __init__(self,filename, mode):
        self.filename=filename
        self.mode=mode
        self.file=None

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,x,y,z):
       self.file.close()
       print("File object has been cleaned up")

with ReadFile('tech.txt','r') as fo:
    print(fo.read())

print(fo.closed)