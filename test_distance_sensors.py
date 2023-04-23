import time
from gpiozero import DistanceSensor 

print('Prepare GPIO Pins')
sensor_1 = DistanceSensor(echo=17, trigger=27, queue_len=2)
sensor_2 = DistanceSensor(echo=5, trigger=6, queue_len=2)

while True: 
    print('Left: {l}, Right: {r}'.format(
        l=sensor_1.distance * 100, 
        r=sensor_2.distance * 100,))
    time.sleep(0.1)
