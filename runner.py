from range_sensor import Sensor
from servo_test import Servo
import time

sensor = Sensor()
servo = Servo()

fire = False

last_activated = 0
first_activated = time.time()

print(time.time())
print(time.time())

try:
    while True:
        distances = sensor.scan()
        fire1 = False
        fire2 = False
        for i in range(len(distances)):
            if distances[i] < 33:
                if not fire1 or fire2:
                    first_activated = time.time()
                if not fire1:
                    fire1 = True
                elif not fire2:
                    fire2 = True
                last_activated = time.time()
            if i == len(distances) - 1:
                fire = fire1 and fire2
        if fire:
            servo.on()
        else:
            servo.off()
except KeyboardInterrupt:
    pass

sensor.done()
servo.done()
