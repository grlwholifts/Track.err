#define wt_N = 1100000
#define speed = 80
#define acc_grav = 9.8
#define mass_kg = 1100000/9.8

input weight_

mass_ = weight_/9.8

allowed_speed = 80*9.9*mass_/110000

input speed_actual

if curve:
	input r
	input theta
	speed_max = sqrt(r*9.8*tan(theta))*3.6

else:
	allowed_speed = speed_max

speed_critical = minimum(allowed_speed,speed_max)

if speed_actual<speed_critical:
	print("OK")

if speed_actual>speed_critical:
	print("slow down")

else:
	print("critical speed reached")
	

