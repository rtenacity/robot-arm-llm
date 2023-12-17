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
        
    def calibrate(self):
        print('calibrating')
        for motor in self.motor_list:
            print(motor)
            calibrated = False
            while calibrated == False:
                if self.btn.left:
                    motor.on_for_degrees(50, 10)
                elif self.btn.right:
                    motor.on_for_degrees(50, -10)
                elif self.btn.up:
                    motor.on_for_degrees(20, 2)
                elif self.btn.down:
                    motor.on_for_degrees(20, -2)
                elif self.btn.enter:
                    calibrated = True
                sleep(0.08)