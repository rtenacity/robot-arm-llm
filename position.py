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
        return self.x, self.y, self.z

    def __str__(self):
        return f"x={self.x}, y={self.y}, z={self.z})"

def get_length(pos1, pos2):
    p1, p2 = pos1.get_pos(), pos2.get_pos()
    return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(3)))

def extend_to_length(pos, length):
    shortened_length = get_length(Position(0,0,0), pos)
    ratio = length/shortened_length
    x, y, z = pos.get_pos()
    x *= ratio
    y *= ratio
    z *= ratio
    
    return Position(x, y, z)

def angles_to_move(pos1, pos2):
    x1, y1, z1 = pos1.get_pos()
    x2, y2, z2 = pos2.get_pos()
    xy_theta = math.acos(((x1 * x2) + (y1 * y2))/( (math.sqrt(x1**2 + y1**2)) * (math.sqrt(x2**2 + y2**2))))
    
    xy_degrees = math.degrees(xy_theta)
    
    yz_theta = math.acos(((y1 * y2) + (z1 * z2))/( (math.sqrt(y1**2 + z1**2)) * (math.sqrt(y2**2 + z2**2))))
    
    yz_degrees= math.degrees(yz_theta)
    
    return xy_degrees, yz_degrees

def move_to_point(pos1, pos2):
    origin = Position(0, 0, 0) 
    init_pos = pos1
    target_pos = pos2
    init_adjusted_pos = extend_to_length(init_pos, get_length(origin, target_pos))   
    angles = angles_to_move(init_adjusted_pos, target_pos)
    return init_adjusted_pos.__str__(), angles

#* CODE TESTING


init_pos = Position(0, 2, 0)
target_pos = Position(2, 2, 0)
instructions = move_to_point(init_pos, target_pos)
print(instructions)