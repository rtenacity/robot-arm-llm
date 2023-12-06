from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor
from ev3dev2.sensor.lego import GyroSensor, TouchSensor
from ev3dev2.button import Button
from time import sleep

revolver = LargeMotor(OUTPUT_A)
shoulder = LargeMotor(OUTPUT_B)
elbow = LargeMotor(OUTPUT_C)
claw = MediumMotor(OUTPUT_D)
gyro = GyroSensor()
touch = TouchSensor()
gyro.MODE_GYRO_G_A()
btn = Button()
motor_list = [revolver, shoulder, elbow, claw]


def calibrate():
    for motor in motor_list:
        calibrated = False
        while calibrated == False:
            if btn.left():
                motor.on_for_degrees(50, 10)
            elif btn.right():
                motor.on_for_degrees(50, -10)
            elif btn.up():
                motor.on_for_degrees(20, 2)
            elif btn.down():
                motor.on_for_degrees(20, -2)
            elif btn.enter():
                calibrated = True
            
def initialize(cal_speed):
    calibrate()
    touch.wait_for_bump()
    gyro.calibrate()
    
def move_to_point(x, y, z, speed=50):
    pass

def main():
    pass