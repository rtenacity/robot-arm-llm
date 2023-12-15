import math

class Position:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def update(self, x=None, y=None, z=None):
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y
            if z is not None:
                self.z = z
                
    def get_pos(self):
        return [self.x, self.y, self.z]
                
    def __str__(self):
        return f"Coordinate(x={self.x}, y={self.y}, z={self.z})"


