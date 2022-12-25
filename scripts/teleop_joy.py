#!/usr/bin/env python

import numpy as np
import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import sys


class CarJoy():
	def __init__(self):
		rospy.init_node('car_control_joy', anonymous=True)
		self.vel_pub = rospy.Publisher('/teleop_cmd_vel', Twist, queue_size=1)
		self.joy_subscriber = rospy.Subscriber('/joy', Joy, self.callback)
		self.rate = rospy.Rate(20)

	def callback(self, data):
		self.joy_b = data.buttons
		self.joy_a = data.axes
		vel = Twist()
		if self.joy_b[4] == 1:
			vel.linear.x = self.joy_a[1]*50
			vel.angular.z = self.joy_a[0]*30
		self.vel_pub.publish(vel)
		rospy.loginfo("publish velocity command[{}PWM, {}PWM]".format(vel.linear.x,vel.angular.z))

if __name__=='__main__':
	try:
		rospy.loginfo("starting joy")
		CarJoy()
		rospy.spin()
	
	except KeyboardInterrupt:
		print "Shutting down"
	

		

