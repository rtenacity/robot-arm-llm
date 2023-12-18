from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor

revolver = LargeMotor(OUTPUT_A)
revolver.reset()

revolver.position = 45
print(revolver.position)
revolver.on_for_degrees(5, 45)
print(revolver.position)
revolver.on_for_degrees(5, 45)
print(revolver.position)
