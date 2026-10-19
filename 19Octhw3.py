
class Table:
    shape = "Rectangular"
    seat = 5
    color = "Brown"
    def __init__(self,s,t,c):
        self.shape = s
        self.seat = t
        self.color = c

print(Table.shape)
print(Table.seat)
print(Table.color)