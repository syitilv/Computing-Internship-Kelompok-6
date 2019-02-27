class vehicle:
    def __init__ (self, year, price):
        self.year = year
        self.price = price
    def ambilnilai(self):
        return self.price


class car:
    def __init__(self, wheel_count, capacity):
        self.wheel_count = wheel_count
        self.capacity = capacity


    def pay_tax(self, price):
        tax = price*0.15
        return tax

    def park(self, hour):
        if self.capacity<3:
            return (self.wheel_count*1250)*hour
        elif self.capacity>5:
            return ((self.wheel_count*1250)*hour)+5000

class motorbike:
    def __init__(self, wheel_count, capacity):
        self.wheel_count = wheel_count
        self.capacity = capacity

    def pay_tax(self, price):
        tax = price*0.10
        return tax

    def park(self, hour):
        if self.capacity<3:
            return(self.wheel_count*1250)*hour
        elif self.capacity>5:
            return ((self.wheel_count*1250)*hour)+5000

class bicycle:
    def __init__(self, wheel_count, capacity):
        self.wheel_count = wheel_count
        self.capacity = capacity

    def pay_tax(self, price):
        tax = price*0
        return tax
    
    def park(self, hour):
        if self.capacity<3:
            return(self.wheel_count*1250)*hour
        elif self.capacity>5:
            return ((self.wheel_count*1250)*hour)+5000
