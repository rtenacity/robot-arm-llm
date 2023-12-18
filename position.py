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
        return "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)

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
    yz_theta = math.acos(((y1 * y2) + (z1 * z2))/( (math.sqrt(y1**2 + z1**2)) * (math.sqrt(y2**2 + z2**2))))
    xy_degrees = round(math.degrees(xy_theta))

    yz_degrees= round(math.degrees(yz_theta), 5)

    return [xy_degrees, yz_degrees]

def get_instructions(pos1, pos2):
    origin = Position(0, 0, 0) 
    init_pos = pos1
    target_pos = pos2
    init_adjusted_pos = extend_to_length(init_pos, get_length(origin, target_pos))   
    angles = angles_to_move(init_adjusted_pos, target_pos)
    return init_adjusted_pos.__str__(), angles


def get_length_and_angle(l1, ang1, l2, ang2):
    v1x = l1 * math.cos(math.radians(ang1))
    v1y = l1 * math.sin(math.radians(ang1))
    v2x = l2 * math.cos(math.radians(ang2))
    v2y = l2 * math.sin(math.radians(ang2))
    length = math.sqrt((v1x + v2x)**2 + (v1y + v2y)**2)
    angle = math.degrees(math.atan2((v1y + v2y), (v1x + v2x)))
    return [length, angle]

def get_coordinates(length, alpha, beta, offset):
    x = (length * math.sin(math.radians(beta)) * math.sin(math.radians(alpha))) - (offset*math.sin(math.radians(alpha)))
    y = length * math.cos(math.radians(beta)) - (offset*math.cos(math.radians(alpha)))
    z = length * math.sin(math.radians(beta)) * math.cos(math.radians(alpha)) 
    return Position(x, y, z)

def get_angles_triangle(a, b, c):
    c_theta = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    a_theta = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    b_theta = math.pi - a_theta - c_theta

    return [math.degrees(a_theta), math.degrees(b_theta), math.degrees(c_theta)]

a, b, c = 3, 4, 5
angles = get_angles_triangle(a, b, c)
print(angles) 


#* CODE TESTING

print(get_coordinates(12.934313455158016, 0, 22.5, 1))

# init_pos = Position(0, 2, 0)
# target_pos = Position(0, 2, 2)
# instructions = get_instructions(init_pos, target_pos)
# print(instructions)