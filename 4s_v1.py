## Sign publisher

#!/usr/bin/env python3
import rospy
import cv2
import time
from std_msgs.msg import Int8
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()


#def subscriber():
#	sub = rospy.Subscriber('/pub_image', Image, get_image)
#	rospy.spin()

def get_image(data):
	#pub = rospy.Publisher('/traffic_sign', Int8, queue_size=10)
	#rate = rospy.Rate(1)
	#message = Int8()

	#while not rospy.is_shutdown():
		#cap = cv2.VideoCapture(0)
		#cap.set(4, 480)
		#cap.set(3, 360)term
		#time.sleep(5)
		message = Int8()
		rospy.loginfo("Node Started")
		stop_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_stop_sign.xml')

		img = bridge.imgmsg_to_cv2(data, 'bgr8')
		#img = cv2.imread('img1')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		stop_sign_scaled, rejectLevels, levelWeights = stop_sign.detectMultiScale3(gray, 1.3, 5, outputRejectLevels=1)
		if len(stop_sign_scaled) > 0:
				message.data = 1
		else:
				message.data = 0
		pub.publish(message.data)
		#rate.sleep()
		#rospy.loginfo("Node Stopped")

if __name__ == '__main__':
	rospy.init_node('traffic_sign_node')
	sub = rospy.Subscriber('/pub_image', Image, get_image)
	while not rospy.is_shutdown():
		pub = rospy.Publisher('/traffic_sign', Int8, queue_size=10)
		rate = rospy.Rate(1)


    
    
#### image publisher


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
		#cap = cv2.VideoCapture(0)
		#cap.set(4, 480)
		#cap.set(3, 360)
		#time.sleep(5)
		#rospy.loginfo("Node Started")
		img = cv2.imread('img2.jpg')
		msg = bridge.cv2_to_imgmsg(img, 'bgr8')
		pub.publish(msg)
		#rate.sleep()
	rospy.loginfo("Node Stopped")

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass

