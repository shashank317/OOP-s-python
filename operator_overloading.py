class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y - other.y)
   
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __eq__(self, other):
        return Vector(self.x == other.x, self.y == other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    

v1 = Vector(10, 20)
v2 = Vector(30, 40)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2
print(v3)  # Output: Vector(40, 60)
print(v4)  # Output: Vector(-20, -20)   



