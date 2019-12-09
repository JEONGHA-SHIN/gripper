#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import rospy

from std_msgs.msg import Float32
 
pin = 18 # PWM pin num 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.setup(22, GPIO.IN)
p = GPIO.PWM(pin, 50)
p.start(0)

angle = 0

while GPIO.input(22)<1:
		p.ChangeDutyCycle(14)
		time.sleep(15)
		

def grab():
	global angle
	while GPIO.input(22)<1:
		p.ChangeDutyCycle(14)
		time.sleep(0.05)
	angle =- 1

def release():
	global angle
	while GPIO.input(4)<1:
 		p.ChangeDutyCycle(1)
  	time.sleep(0.05)
	angle =+ 1

def angle_cb(msg):
	if angle < msg.data-3 & angle > msg.data+3
		while angle <	msg.data
			release()
		while angle > msg.data
			grab()
		
def key_cb(msg):
	if msg.data	>	0:
		release()
	elif msg.data <0:
		grab()

	
		
rospy.init_node('gripper')
gripper_pub = rospy.Publisher('/gripper/status', Float32, queue_size=1)
rospy.Subscriber('/gripper/move/angle', Float32, angle_cb)
rospy.Subscriber('/gripper/move/key', Float32, key_cb)

gripper_pub.publish(angle)

rospy.spin()


