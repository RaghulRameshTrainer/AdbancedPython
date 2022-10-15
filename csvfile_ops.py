import csv

# with open(r'C:\Users\RaghulRamesh\OneDrive\Desktop\data\employee.csv','r') as fo:
#     csv_obj=csv.reader(fo)
#     for row in csv_obj:
#         print(f"Empid:{row[0]}, EmpName:{row[1]}, City:{row[2]}")

with open('newfile.csv','w',newline='') as fo:
    obj=csv.writer(fo)
    obj.writerow([1,'Laptop',70000,'Lennova','Bangalore'])
    obj.writerow([2,'Desktop',50000,'Dell','Hyderabad'])