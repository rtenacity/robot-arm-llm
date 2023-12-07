import math

class Position:
    def __init__(self):
        self.x = 5
        self.y = 0
        self.z = 0
    
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
        
    def set_z(self, z):
        self.z = z
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z
    
    def xyz_dist(self, x1, y1, z1, x2, y2, z2):
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        return dist
    
    def xy_dist(self, x1, y1, x2, y2):
        dist = math.sqrt((x2-x1)**2 + (y2-y1) ** 2)
    