
class employee:
    company = "google"
    def __init__(self , ID_number , Shift , name ): 
        self.ID_number = ID_number
        self.Shift = Shift
        self.name = name

    def GetInfo(self):
        print(f"The name of the employee of {self.company} is {self.name} and his ID number is {self.ID_number} and work for {self.Shift} ")

Nischay = employee(12234543 , "Morning shift" , 'Nischay')

Nischay.GetInfo()

        


