import RPi.GPIO as GPIO
import time

class Sensor:
    
    TRIG = 23
    ECHO = 24
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        print("Distance measurement in progress")

        GPIO.setup(Sensor.TRIG, GPIO.OUT)
        GPIO.setup(Sensor.ECHO, GPIO.IN)

        GPIO.output(Sensor.TRIG, False)
        print("Waiting for sensor to settle")

        time.sleep(2)

        print("Activating")
        
    def scan(self):
        distances = []
        for i in range(10):
                          
            GPIO.output(Sensor.TRIG, True)
            time.sleep(0.00001)
            GPIO.output(Sensor.TRIG, False)

            while (GPIO.input(Sensor.ECHO)==0):
                pulse_start = time.time()
            while (GPIO.input(Sensor.ECHO)==1):
                pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
            distance = round(distance, 2)
            
            distances.append(distance)

            print("Distance: " + str(distance)+"cm")
            time.sleep(.05)
        return distances

    def done(self):
        GPIO.cleanup()
