from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor
from ev3dev2.sensor.lego import GyroSensor, TouchSensor
from ev3dev2.button import Button
from time import sleep
import math
from position import Position

revolver = LargeMotor(OUTPUT_D)
shoulder = LargeMotor(OUTPUT_C)
elbow = LargeMotor(OUTPUT_B)
claw = MediumMotor(OUTPUT_A)
touch = TouchSensor()
btn = Button()
motor_list = [revolver, shoulder, elbow, claw]
initial = Position(0,0,0)
pos = Position()

def increase_arm_length_3d(pos1, new_length):
    temp_x = pos1.get_x()
    temp_y = pos1.get_y()
    temp_z = pos1.get_z()

    # TODO: Make the angle from the motor encoder rather than calculating it using x and y 
    
    angle_xy = math.atan2(temp_y, temp_x)

    new_x = new_length * math.cos(angle_xy)
    new_y = new_length * math.sin(angle_xy)

    # TODO: Add logic for moving arm forward and backward after configuration is set up
      
    return new_x, new_y, temp_z 


    

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
