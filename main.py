from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor
from ev3dev2.sensor.lego import GyroSensor

revolver = LargeMotor(OUTPUT_A)
shoulder = LargeMotor(OUTPUT_B)
elbow = LargeMotor(OUTPUT_C)
claw = MediumMotor(OUTPUT_D)
gyro = GyroSensor()

def calibrate(motor, angle, vel):
    while motor.position() < angle or motor.position() > 0:
        if motor.position() < angle:
            motor.on(vel)
        else: 
            revolver.on(-vel)
            

def initialize(cal_speed):
    calibrate(revolver, 0, cal_speed)   
    print("revolver calibrated")
    
    calibrate(shoulder, 90, cal_speed)
    print("shoulder calibrated")
    
    calibrate(elbow, 90, cal_speed)
    print("elbow calibrated")
    
    calibrate(claw, 0, cal_speed*0.5)
    print("claw calibrated")
    

def main():
    pass