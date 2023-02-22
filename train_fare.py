class Train:
    def __init__(self , name , fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The no. of seats available in the train are {self.seats}")

    def fareInfo(self):
        print(f"The fare of the train is {self.fare}")

    def BookTicket(self):
        if(self.seats>0):
            print(f"you seat has been booked and your seat number is {self.seats}")

        else:
            print("There are no seat left kindly try in tatkal")

intercity = Train("Lucknow chandigarh express" , 190 , 300)

intercity.getStatus()
intercity.fareInfo()


   