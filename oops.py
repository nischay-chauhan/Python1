class employee:
    company = "google"
    salary = 100

Nischay = employee()
Harman = employee()
Nischay.salary = 300
Harman.salary = 100

print(Nischay.salary)
print(Harman.salary)
print(Nischay.company)
print(Harman.company)


#code for oops
class employee:
    company = "google"
    def Getsalary(self):
        print(f"Salary of this employee in {self.company} is {self.salary}")

Nischay = employee()
Nischay.salary = "$250,000"
Nischay.Getsalary()

# code _03 for oops

class Programmer:
    company = "Microsoft"

    def __init__(self , name , product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

Nischay = Programmer("Nischay" , "Skype")
Alka = Programmer("Alka" , "Zoom")
Nischay.getInfo()
Alka.getInfo()

