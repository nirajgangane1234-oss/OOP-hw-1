
class Light:
    brand = "Phillips"
    type = "LED"
    price = 200

    def __init__(self,b,t,p):
        self.brand = b
        self.type = t
        self.price = p

print(Light.brand)
print(Light.type)
print(Light.price)