import math

class Position:
    def __init__(self, x=0, y=0, z=0):
        self.x = x  # Left-Right
        self.y = y  # Forward-Backward
        self.z = z  # Up-Down

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

def get_length(pos1, pos2):
    p1, p2 = pos1.get_pos(), pos2.get_pos()
    return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(3)))



