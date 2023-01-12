#!/usr/bin/env python
import rospy, math, tf2_ros, geometry_msgs.msg, turtlesim.srv, math

if __name__ == '__main__':

    rospy.init_node('tf2_turtlebot3_follower')
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    turtlebot_vel = rospy.Publisher('/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform("base_footprint", "nav_goal_tf", rospy.Time())
            # print(trans.transform)
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        msg = geometry_msgs.msg.Twist()

        msg.angular.z = 1.5 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
        msg.linear.x = 0.5 * math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2)

        w = msg.angular.z
        l = msg.linear.x

        # max angular velocity 2.8 rad/s
        if abs(w) > 2.8:
            msg.angular.z = math.copysign(1, w)*2.8
            
        # max linear velocity 0.22 m/s
        if l > 0.22:
            msg.linear.x = 0.22

        turtlebot_vel.publish(msg)
        
        rate.sleep()