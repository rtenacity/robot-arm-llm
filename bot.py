from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor
from ev3dev2.sensor.lego import GyroSensor, TouchSensor
from ev3dev2.button import Button
from time import sleep
from position import Position, get_instructions

class Bot:
    def __init__(self, revolver, shoulder, elbow, claw) -> None:
        self.revolver = LargeMotor(revolver)
        self.shoulder = LargeMotor(shoulder)
        self.elbow = LargeMotor(elbow)
        self.claw = MediumMotor(claw)
        self.btn = Button()
        self.motor_list = [self.revolver, self.shoulder, self.elbow, self.claw]
        self.pos = None
        self.ang1 = None
        self.ang2 = None
        
    def reset(self):
        for motor in self.motor_list:
            motor.reset()
        
    def calibrate(self):
        print('calibrating')
        for motor in self.motor_list:
            print(motor)
            calibrated = False
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
            
    def initialize(self):
        self.reset()
        self.calibrate()