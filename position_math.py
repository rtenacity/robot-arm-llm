import math
from position import Position

def get_length(pos1, pos2):
    p1 = pos1.get_pos()
    p2 = pos2.get_pos()
    dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
    return dist

def get_xy_theta():
    pass
    