from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor
from ev3dev2.sensor.lego import GyroSensor, TouchSensor
from ev3dev2.button import Button
from time import sleep
from position import *

class Bot:
    def __init__(self, revolver, shoulder, elbow, claw) -> None:
        self.shoulder_port = shoulder
        self.revolver = LargeMotor(revolver)
        self.shoulder = LargeMotor(shoulder)
        self.elbow = LargeMotor(elbow)
        self.claw = MediumMotor(claw)
        self.btn = Button()
        self.shoulder_length = 6 #temp 
        self.elbow_length = 3.75 #temp
        self.motor_list = [self.revolver, self.shoulder, self.elbow, self.claw]
        self.back_offset = 2.8 # (9.4 * 0.32) <- could change
        self.vertical_offset = 3 # (9.4 * 0.32) <- could change
        self.pos = None
        self.revolver_vertical_angle = None
        
    def reset(self):
        for motor in self.motor_list:
            motor.reset()
            
    def motor_still(self):
        for motor in self.motor_list:
            motor.on_for_degrees(0, 0)
            
    def get_pos(self):
        return self.pos.__str__()
        
    def calibrate(self):
        print('calibrating')
        for motor in self.motor_list:
            print(motor)
            calibrated = False
            if motor == self.shoulder:
                print("shoulder")

                while calibrated == False:
                    move = input("hjkl (y): ")
                    if move == 'h':
                        motor.on_for_degrees(50, 10)
                    elif move == 'l':
                        motor.on_for_degrees(50, -10)
                    elif move == 'j':
                        motor.on_for_degrees(20, 2)
                    elif move == 'k':
                        motor.on_for_degrees(20, -2)
                    elif move == 'y':
                        calibrated = True
                    else:
                        pass
                    sleep(0.08)
                pos_f = motor.position
                motor.reset()
                motor.on_for_degrees(50, 0)
            else:
                while calibrated == False:
                    move = input("hjkl (y): ")
                    if move == 'h':
                        motor.on_for_degrees(50, 10)
                    elif move == 'l':
                        motor.on_for_degrees(50, -10)
                    elif move == 'j':
                        motor.on_for_degrees(20, 2)
                    elif move == 'k':
                        motor.on_for_degrees(20, -2)
                    elif move == 'y':
                        calibrated = True
                    else:
                        pass
                    sleep(0.08)
                motor.reset()
                motor.on_for_degrees(50, 0)
        
    def calculate_position(self):
        length, beta = get_length_and_angle(self.shoulder_length, self.shoulder.position+45, self.elbow_length, self.elbow.position)
        self.pos = get_coordinates(length=length, alpha=self.revolver.position, beta=beta, back_offset=self.back_offset, vertical_offset=self.vertical_offset)
        
    def initialize(self):
        self.reset()
        self.motor_still()
        self.calibrate()
        self.calculate_position()
        
        
    def move_to_point(self, target_pos):
        alpha, beta = angles_to_move(self.pos, target_pos)
        tx, ty, tz = self.pos.get_pos()
        tx += self.back_offset*math.sin(math.radians(alpha))
        ty += self.back_offset*math.cos(math.radians(alpha))
        current_pos = Position(tx, ty, tz)
        
        reached = False
        #TODO: implement PID for the point
        
        
        tempX, tempY, tempZ = target_pos.get_pos()
        
       
        tempX += self.back_offset*math.sin(math.radians(alpha))
        tempY += self.back_offset*math.cos(math.radians(alpha))
        target_pos = Position(tempX, tempY, tempZ)
        
        target_length = get_length(Position(0, 0, 0), target_pos)
        a, b, c = get_angles_triangle(self.shoulder_length, self.elbow_length, target_length)
        
        b_theta = (45 + self.shoulder.position) - b # temp
        c_theta = (135 + self.elbow.position) - c # temp
        
        
        if b_theta >= 0: 
            print("big money")
            self.shoulder.on_for_degrees(50, b_theta, block = False) 
        else:
            print("nah not happening")
            self.shoulder.on_for_degrees(5, b_theta, block = False)
        
        self.elbow.on_for_degrees(5, c_theta)
        
        
        self.calculate_position()
        xy_theta, yz_theta = angles_to_move(self.pos, target_pos)
        self.revolver.on_for_degrees(50, -xy_theta)
        self.shoulder.on_for_degrees(10, -yz_theta)
        self.calculate_position()
        