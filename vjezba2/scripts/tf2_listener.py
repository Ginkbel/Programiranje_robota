#!/usr/bin/env python
import rospy, tf2_ros, geometry_msgs.msg
if __name__ == '__main__':
    rospy.init_node('tf2_listener')
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    rate = rospy.Rate(10.0)
    
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('turtle1', 'world', rospy.Time())
            x = trans.transform.translation.x
            y = trans.transform.translation.y
            print("x = " + str(x) + "\n")
            print("y = " + str(x) + "\n")
            rate.sleep()
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
        continue