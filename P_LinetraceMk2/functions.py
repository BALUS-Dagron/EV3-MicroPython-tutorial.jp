#モジュールのテストかねてimportできるかな

def R_cal():
    """R_sens の値を 0-100 にcalibration"""
    return (( R_sens.reflection() - R_BLACK) / ( R_WHITE - R_BLACK))*100
