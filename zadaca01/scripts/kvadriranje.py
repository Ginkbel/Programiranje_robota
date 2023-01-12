#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

kvadrat_broja = Int64()

def callback(data):

    global kvadrat_broja
    kvadrat_broja = data.data**2
    rospy.loginfo('Kvadrat broja: %s', kvadrat_broja)

def kvadriranje():

    rospy.init_node('Kvadraticar', anonymous=True)
    rospy.Subscriber('broj', Int64, callback)
    pub = rospy.Publisher('kvadrat_broja', Int64, queue_size=10)
    
    while not rospy.is_shutdown():
        if kvadrat_broja is not None:
            pub.publish(kvadrat_broja)
        rospy.sleep(0.5)  # 2 Hz

if __name__ == '__main__':
    kvadriranje()
