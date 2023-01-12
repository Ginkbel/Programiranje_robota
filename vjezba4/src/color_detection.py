#!/usr/bin/env python
from __future__ import print_function
import roslib
roslib.load_manifest('vjezba4')
import sys
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

	def __init__(self):
		self.image_pub = rospy.Publisher("image_topic_2",Image)
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/image_raw",Image,self.callback)
		
	def callback(self,data):

		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)
			
		(rows,cols,channels) = cv_image.shape
		
		if cols > 60 and rows > 60 :
			cv2.circle(cv_image, (50,50), 10, 255)
		
		# convert to hsv colorspace
		hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

		# lower bound and upper bound for Green color
		lower_bound = np.array([50, 20, 20])	 
		upper_bound = np.array([100, 255, 255])

		# find the colors within the boundaries
		mask = cv2.inRange(hsv, lower_bound, upper_bound)
		
		#define kernel size  
		kernel = np.ones((7,7),np.uint8)

		# Remove unnecessary noise from mask

		mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
		mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
		
		# Segment only the detected region
		segmented_img = cv2.bitwise_and(cv_image, cv_image, mask=mask)
		
		# Find contours from the mask

		contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)

		# Showing the output

		cv2.imshow("Output", output)
				
		cv2.imshow("Slika", mask)
		cv2.waitKey(3)
		
		try:
			self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
		except CvBridgeError as e:
			print(e)

def main(args):
	
	ic = image_converter()
	rospy.init_node('image_converter', anonymous=True)
	
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()
	
if __name__ == '__main__':
	main(sys.argv)


