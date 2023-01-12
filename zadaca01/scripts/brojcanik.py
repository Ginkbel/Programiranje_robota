#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def brojac():
    
    pub = rospy.Publisher('broj', Int64, queue_size=10)
    rospy.init_node('Brojac', anonymous=True)
    rate = rospy.Rate(2) # 2 Hz
    x = 0
    
    while not rospy.is_shutdown():
        
        hello_str = "Broj: %s" % x
        rospy.loginfo(hello_str)
        pub.publish(x)
        x += 1
        rate.sleep()
        

if __name__ == '__main__':
    try:
        brojac()
    except rospy.ROSInterruptException:
        pass