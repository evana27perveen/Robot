from gpiozero import Servo
from time import sleep

servoH, servoRHU, servoRHD, servoLHU, servoLHD = Servo(14),  Servo(15),  Servo(18),  Servo(23),  Servo(24)

while True:
    servoH.mid()
    sleep(2)
    servoH.max()
    sleep(1)
    servoH.mid()
    sleep(2)
    servoH.min(1)