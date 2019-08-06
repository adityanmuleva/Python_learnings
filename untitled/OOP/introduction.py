"""
CLASS - Template for creating an object.All objects created under same class
        have same characteristic.
OBJECTS - An instance of class.
INSTANTIATE - Create an instance in class.
METHOD - Functions in class
ATTRIBUTE - A variable bounded to an instance of class.
SELF - Reference of the instance of the class
"""


class Kettle(object):

    PowerSource = "Electricity"

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.on = False


milton = Kettle("Milton", 550)
print(milton.name)
print(milton.price)

milton.price = 600
print(milton.price)

nike = Kettle("Nike", 1500)
print(nike.name)
print(nike.price)

print("OVERALL PRICE FOR :- \n{} is {}\n{} is {} ".format(milton.name, milton.price, nike.name, nike.price))
print("="*80)
print(Kettle.PowerSource)

print("Switching power source to atomic")

Kettle.PowerSource = "Atomic"
print(Kettle.PowerSource)
milton.PowerSource = "Gas"
print(milton.PowerSource)
print(nike.PowerSource)

print(Kettle.__dict__)
print(milton.__dict__)
print(nike.__dict__)
