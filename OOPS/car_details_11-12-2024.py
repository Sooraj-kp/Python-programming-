class car:
    company=0
    price=0
    color=0

    def car_details(self):
        print("company : ", self.company)
        print("price : ",self.price)
        print("color : ",self.color)
        print()
        print()

car1=car()
car1.company="TOYOTA"
car1.price=30000000
car1.color="RED"
print("DETAILS OF FIRST CAR")
car1.car_details()




car1=car()
car1.company="BMW"
car1.price=50000000
car1.color="BLACK"
print("DETAILS OF SECOND CAR")
car1.car_details()
    




car1=car()
car1.company="LAND ROVER"
car1.price=70000000
car1.color="WHITE"
print("DETAILS OF THIRD CAR")
car1.car_details()
        
