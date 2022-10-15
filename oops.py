class Employee():
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@gmail.com'

    # def fullname(self):
    #     return f"{self.fname} {self.lname}"

    def fullname(self,*x):
        if len(x)==3:
            tit,fn,ln=x
            return f"{tit} {fn} {ln}"
        elif len(x)==2:
            tit,name=x
            return f"{tit} {name}"
        else:
            title=x
            return f"{title[0]} {self.fname} {self.lname}"


    def __repr__(self):
        return "This is the Employee class object"
    def __str__(self):
        return "THIS IS THE EMPLOYEE CLASS OBEJECT"

    def __add__(self,other):
        return self.salary+other.salary

    @classmethod
    def create_object(cls,emp_str):
        fn,ln,pay=emp_str.split("-")
        return cls(fn,ln,int(pay))

    @staticmethod
    def is_workingday(d):
        if d.weekday()==5 or d.weekday()==6:
            return "IT'S HOLIDAY"
        return "WORKING DAY"

emp1="Malini-Sekar-50000"
emp2="Tharani-Siva-60000"

emp_1=Employee.create_object(emp1)
emp_2=Employee.create_object(emp2)
print(emp_1.fullname('Mr',"Ashwin", "Sekar"))
# import datetime
# tday=datetime.date(2022,10,8)
# print(Employee.is_workingday(tday))

# INHERITANCE
class Manager():
    def fullname(self,title):
        return f"{title} {self.fname} {self.lname}"

class Customer():
    def fullname(self,title):
        return f"{title} {self.lname} {self.fname}"

class Developer(Employee,Manager,Customer):
    def __init__(self,fname,lname,pay,tech):
        super().__init__(fname, lname, pay)
        self.tech=tech

    def fullname(self,title):
        #return Manager.fullname(self,title)
        return super(Manager,self).fullname(title)

m1=Developer('Siva','Ram',500000,'Python')
# print(m1.email +' and '+m1.tech)
# print(m1.fullname('Mr'))
# print(help(m1))
# emp_1=Employee('Levin','Lenus',10000)
# emp_2=Employee('Rajesh','Kumar',20000)


# print(emp_1.email)
# print(emp_2.email)
#
# print(emp_1+emp_2)
#
# print(emp_1.fullname())
# print(emp_2.fullname())