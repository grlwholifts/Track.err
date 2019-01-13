
# define mass_= 1100000/9.8
from math import sqrt

input weight_

mass_ = weight_ / 9.8

allowed_speed = 80 * 9.9 * mass_ / 110000

input speed_actual

float speed_max

if curve:
    input r
    input theta
    speed_max = sqrt(r * 9.8 * tan(theta)) * 3.6

else:
    allowed_speed = speed_max

speed_critical = minimum(allowed_speed, speed_max)

if speed_actual < speed_critical:
    print("OK")

if speed_actual > speed_critical:
    print("slow down")

else:
    print("critical speed reached")

