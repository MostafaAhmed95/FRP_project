#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(data):
    pub.publish((data.data)*2)
    rospy.loginfo(data.data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/rrbot/joint1_position_controller/command", Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('chatter', Float64, queue_size=10)
    listener()
