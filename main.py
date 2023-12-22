
from bot import Bot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from position import Position

arm = Bot(OUTPUT_A, OUTPUT_C, OUTPUT_B, OUTPUT_D)

arm.initialize()
print(arm.get_pos())
arm.move_to_point(Position(0, 6, 0))
print(arm.get_pos())

# ok so it kind of works now i just need to tune values!!!!!!
# also in order to get thing to work need to slower speed of motors especially shoulder