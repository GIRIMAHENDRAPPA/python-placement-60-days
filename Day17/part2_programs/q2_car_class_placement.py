class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def discount_price(self,percent):
        return self.price - (self.price * percent /100)
c1=Car("BMW",5000000)
print(c1.discount_price(10))