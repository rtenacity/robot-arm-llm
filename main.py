from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor
from ev3dev2.sensor.lego import GyroSensor, TouchSensor
from ev3dev2.button import Button
from time import sleep
import math
from position import Position, get_instructions

revolver = LargeMotor(OUTPUT_D)
shoulder = LargeMotor(OUTPUT_C)
elbow = LargeMotor(OUTPUT_B)
claw = MediumMotor(OUTPUT_A)
touch = TouchSensor()
btn = Button()
motor_list = [revolver, shoulder, elbow, claw]
initial = Position(0,2,0)
pos = None


def calibrate():
    print('calibrating')
    for motor in motor_list:
        print(motor)
        calibrated = False
        while calibrated == False:
            if btn.left:
                motor.on_for_degrees(50, 10)
            elif btn.right:
                motor.on_for_degrees(50, -10)
            elif btn.up:
                motor.on_for_degrees(20, 2)
            elif btn.down:
                motor.on_for_degrees(20, -2)
            elif btn.enter:
                calibrated = True
            sleep(0.08)
            
def initialize(cal_speed):
    print("initializing")
    calibrate()
    touch.wait_for_bump()
    
    
def move_to_point(x, y, z, speed=50):
    pass

def main():
    print("hello")
    initialize(50)
    
main()
