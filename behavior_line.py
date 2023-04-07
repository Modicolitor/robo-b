import robot

from time import sleep

r = robot.Robot()
#r.set_left(80)
#r.set_left(80)
#sleep(1)
r.straight(1)
r.turn_right(0.6)
r.straight(1)
r.turn_left(0.6)
r.straight(2)
r.turn_left(0.6)
r.straight(1)
r.spin_left(1)


