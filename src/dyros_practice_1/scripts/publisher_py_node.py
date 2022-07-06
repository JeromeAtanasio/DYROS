#!/usr/bin/env python
# license removed for brevity
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

def talker():
    # Create Publisher
    pub = rospy.Publisher('/helloros_topic', Int32, queue_size=10) 
    
    # initialize node. "anonymous = True -> prevent node redundancy"
    rospy.init_node('dyros_publisher_node', anonymous=True) 
    rate = rospy.Rate(1) # 1hz
    i = 1
    
     #keep the ROS until it gets end signal
    while not rospy.is_shutdown():
        pub.publish(i)
        i = i + 1
        rate.sleep()
        
# Program enter point
if __name__ == '__main__':
    try:
        talker()
    # ROSnterruptException is the end signal. Stop the program
    except rospy.ROSInterruptException: 
        pass