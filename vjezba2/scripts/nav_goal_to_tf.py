#!/usr/bin/env python

import rospy, tf2_ros, geometry_msgs.msg

def handle_nav_goal_pose(msg):
    
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    
    rospy.sleep(0.1)

    while not rospy.is_shutdown():

        rospy.sleep(0.1)

        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "odom"
        t.child_frame_id = "nav_goal_tf"
        t.transform.translation.x = msg.pose.position.x
        t.transform.translation.y = msg.pose.position.y
        t.transform.translation.z = 0.0
        t.transform.rotation.x = msg.pose.orientation.x
        t.transform.rotation.y = msg.pose.orientation.y
        t.transform.rotation.z = msg.pose.orientation.z
        t.transform.rotation.w = msg.pose.orientation.w

        br.sendTransform(t)

if __name__ == '__main__':

    rospy.init_node('nav_goal_to_tf')
    rospy.Subscriber("/move_base_simple/goal", geometry_msgs.msg.PoseStamped, handle_nav_goal_pose)
    rospy.spin()