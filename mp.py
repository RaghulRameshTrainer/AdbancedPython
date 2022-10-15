import monkey_patch

def function_one():
    print("function_one is being called")

obj=monkey_patch.A()

obj.myfunc=function_one

obj.myfunc()