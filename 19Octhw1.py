class Laptop:
    color = "Black"
    RAM = 64
    brand = "LENOVO"
    def __init__(self,c,r,b):
        self.color = c
        self.RAM = r
        self.brand = b

print(Laptop.color)
print(Laptop.RAM)
print(Laptop.brand)