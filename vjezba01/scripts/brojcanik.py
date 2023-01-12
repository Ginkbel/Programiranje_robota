#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def brojac():
    
    pub = rospy.Publisher('Broj', Int64, queue_size=10)
    rospy.init_node('Brojac', anonymous=True)
    rate = rospy.Rate(2) # 2 Hz
    x = 0
    
    while not rospy.is_shutdown():
        
        hello_str = rospy.get_caller_id() + "Broj: %s" % x
        rospy.loginfo(hello_str)
        pub.publish(x)
        rate.sleep()
        x += 1

if __name__ == '__main__':
    try:
        brojac()
    except rospy.ROSInterruptException:
        pass