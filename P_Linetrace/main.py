#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

R_motor = Motor(Port.C,Direction.CLOCKWISE)
L_motor = Motor(Port.B,Direction.CLOCKWISE)
R_sens = ColorSensor(Port.S3)
L_sens = ColorSensor(Port.S1)

R_w = 86
R_b =10
R_range = R_w - R_b
L_w =90
L_b =8
L_range = L_w - L_b

R_bef=0
L_bef=0

P_base =1000
kp =0

R_pow=0
L_pow=0

differential = 0
correction = 0

i=1

# Write your program here.
ev3.speaker.beep()

while i == 1:
    R_bef = R_sens.reflection()
    L_bef = L_sens.reflection()
    differential = ((R_bef-R_b)/R_range - (L_bef-L_b)/L_range)
    R_pow = P_base + differential * kp + correction
    L_pow - P_base - differential * kp - correction
    R_motor.run(R_pow)
    L_motor.run(L_pow)


    
