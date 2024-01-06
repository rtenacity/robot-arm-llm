
from bot import Bot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from position import Position
arm = Bot(OUTPUT_A, OUTPUT_C, OUTPUT_B, OUTPUT_D)

def main():
    arm.initialize()
    print(arm.get_pos())
    arm.move_to_point(Position(0, 5, 0))
    print(arm.get_pos())
    
if __name__ == '__main__':
    main()


#! Z value is inverted, need to change calculate position function
#! Tune values
#! Need to calculate end effector position
