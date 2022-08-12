class Vehicles():
    def __init__(self, id, type, premium_amt):
        self.id = id
        self.type = type
        self.premium_amt = premium_amt

    def Details(self):
        if(self.type == "Two Wheeler"):
            print(f"The Id is {self.id}")
            print(f"The Type is {self.type}")
            print(
                f"The premium amt will be {self.premium_amt+(self.premium_amt*0.02)}")
        elif(self.type == "Four Wheeler"):
            print(f"The Id is {self.id}")
            print(f"The Type is {self.type}")
            print(
                f"The premium amt will be {self.premium_amt+(self.premium_amt*0.06)}")
        else:
            print("Invalid Type")


bike = Vehicles(1, "Two Wheeler", 2000)
bike.Details()
