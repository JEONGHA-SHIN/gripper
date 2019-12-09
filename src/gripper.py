import RPi.GPIO as GPIO
import time
 
pin = 18 # PWM pin num 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.setup(22, GPIO.IN)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0
try:
	while GPIO.input(4)<1:
 		p.ChangeDutyCycle(1)
  	time.sleep(1)
	while GPIO.input(22)<1:
		p.ChangeDutyCycle(14)
		time.sleep(1)
		
except KeyboardInterrupt:
		p.stop()
GPIO.cleanup()


