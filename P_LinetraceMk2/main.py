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

#
#センサ2つでPDライントレースを延々とするだけのプログラム
#

ev3 = EV3Brick()
R_motor = Motor(Port.B,Direction.CLOCKWISE)
L_motor = Motor(Port.C,Direction.CLOCKWISE)
R_sens = ColorSensor(Port.S2)
L_sens = ColorSensor(Port.S3)
timer = StopWatch()

#initializing
R_WHITE = 98
R_BLACK = 4
L_WHITE = 98
L_BLACK = 3
#基本の速度 [mm/s]
BASE_SPEED = 500
#比例/微分ゲイン
Kp = 1
Kd = 0
#旋回傾向があるときの補正用．正の値を入れて左旋傾向にできる．
CORRECTION = 0
#黒線に対するロボットの位置
potition_now = 0
position_before = 0

def R_cal():
    """R_sens の値を 0-100 にcalibration"""
    return (( R_sens.reflection() - R_BLACK) / ( R_WHITE - R_BLACK))*100


def L_cal():
    """L_sens の値を 0-100 にcalibration"""
    return (( L_sens.reflection() - L_BLACK) / ( L_WHITE - L_BLACK))*100

def position(right_sens, left_sens):
    """ロボットの現在位置
    left, right の calibration 済みの値から出す．
    黒線より左よりで negative，右よりで positive の値を返す
    範囲 -100~100
    右白で100 左黒で0 このときposition (100-0)/100=1
    右黒で0 左白で100 このときposition (0-100)/100=-1
    """
    return (right_sens - left_sens) / 100


def drive(drive_bias):
    R_motor.run(BASE_SPEED * ( 1 + drive_bias + CORRECTION ) )
    L_motor.run(BASE_SPEED * ( 1 - drive_bias - CORRECTION ) )

# Write your program here.

ev3.speaker.beep()

while True:
    position_now = position(R_cal(), L_cal())
    delta_position = ( position_before - position_now) / timer.time()
    position_before = position_now
    #微分用時計リセット
    timer.reset()
    #制御量算出
    bias = position( R_cal(), L_cal() ) * Kp + delta_position * Kd
    #実際の駆動
    drive( bias )
    #waitはいらないかも
    wait(20)