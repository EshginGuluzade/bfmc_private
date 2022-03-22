#!/usr/bin/env python3
import rospy
import cv2
import time
from std_msgs.msg import Int8
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def publisher():
	pub = rospy.Publisher('/pub_image', Image, queue_size=1)
	rospy.init_node('image_node', anonymous=False)
	rospy.Rate(10)

	while not rospy.is_shutdown():		
		img = cv2.imread('nimg.jpg')
		msg = bridge.cv2_to_imgmsg(img, 'bgr8')
		pub.publish(msg)
		#rate.sleep()
	rospy.loginfo("Node Stopped")

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass

