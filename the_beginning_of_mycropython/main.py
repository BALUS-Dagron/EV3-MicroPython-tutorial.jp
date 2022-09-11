#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Soun dFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
L_motor = Motor(Port.B,Direction.CLOCKWISE)
R_motor = Motor(Port.C,Direction.CLOCKWISE)
Lc = ColorSensor(Port.S1)
Rc = ColorSensor(Port.S3)
i=1


while i==1 :
    if Lc.color() == Color.BLACK:
        L_motor.run(50)
        R_motor.run(100)
    else :
        L_motor.run(100)
        R_motor.run(50)





