#!/usr/bin/env python3
import rospy
import cv2
import time
from std_msgs.msg import Int8
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

# stop_sign = 1
# priority_sign = 2
# parking_sign = 3
# cross_sign = 4
# None = 0

def get_image(data):
		message = Int8()
		#rospy.loginfo("Node Started")
		stop_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_stop_sign.xml')
		priority_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_yield_sign_v2.xml')
		parking_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_park2.xml')
		cross_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_crosswalk_sign_v2.xml')

		img = bridge.imgmsg_to_cv2(data, 'bgr8')
		#img = cv2.imread('img1')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		stop_sign_scaled, rejectLevels, levelWeights = stop_sign.detectMultiScale3(gray, 1.3, 5, outputRejectLevels=1)
		park_sign_scaled, rejectLevels, levelWeights = parking_sign.detectMultiScale3(gray, 1.3, 5, outputRejectLevels=1)
		cross_sign_scaled, rejectLevels, levelWeights = cross_sign.detectMultiScale3(gray, 1.3, 5, outputRejectLevels=1)
		priority_sign_scaled, rejectLevels, levelWeights = priority_sign.detectMultiScale3(gray, 1.3, 5, outputRejectLevels=1)
		
		if len(stop_sign_scaled) > 0:
				message.data = 1
		elif len(priority_sign_scaled) > 0:
				message.data = 2
		elif len(park_sign_scaled) > 0 :
				message.data = 3
		elif len(cross_sign_scaled) > 0:
				message.data = 4

		pub.publish(message.data)
		#rate.sleep()
		#rospy.loginfo("Node Stopped")

if __name__ == '__main__':
	rospy.init_node('traffic_sign_node')
	sub = rospy.Subscriber('/automobile/image_raw', Image, get_image)
	while not rospy.is_shutdown():
		try:
			pub = rospy.Publisher('/traffic_sign_topic', Int8, queue_size=1)
		except ospy.ROSInterruptException:
			pass
		#rate = rospy.Rate(1)
		rospy.spin()

