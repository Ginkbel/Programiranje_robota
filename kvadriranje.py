#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def callback(data):
    kvadrat_broja = data.data**2
    rospy.loginfo(rospy.get_caller_id() + 'Kvadrat broja: %s', kvadrat_broja)
    pub.publish(kvadrat_broja)

def kvadriranje():

    rospy.init_node('Kvadraticar', anonymous=True)
    rospy.Subscriber('Broj', Int64, callback)
    
    pub = rospy.Publisher('Kvadrat broja', Int64, queue_size=10)
    x = 0
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    kvadriranje()