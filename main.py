
from bot import Bot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D

arm = Bot(OUTPUT_A, OUTPUT_C, OUTPUT_B, OUTPUT_D)

arm.initialize()