import RPi.GPIO as GPIO
import time
class Servo:
    
    RED = 5
    GREEN = 6
    SERVO = 17
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(Servo.SERVO, GPIO.OUT)
        GPIO.setup(Servo.RED, GPIO.OUT)
        GPIO.setup(Servo.GREEN, GPIO.OUT)
        
        self.p = GPIO.PWM(Servo.SERVO, 50)
        self.p.start(1.7) #1.5
        time.sleep(.75)
        self.open = False
    
    def on(self):
        if not self.open:
            self.p.ChangeDutyCycle(3.2) #3.2
            self.open = True
            time.sleep(.2)
        GPIO.output(Servo.RED, GPIO.LOW)
        GPIO.output(Servo.GREEN, GPIO.HIGH)
        
    def off(self):
        if self.open:
            self.p.ChangeDutyCycle(1.4) #1.5
            self.open = False
            time.sleep(.5)
        GPIO.output(Servo.RED, GPIO.HIGH)
        GPIO.output(Servo.GREEN, GPIO.LOW)
    
    def done(self):
        GPIO.cleanup()
        self.p.stop()



