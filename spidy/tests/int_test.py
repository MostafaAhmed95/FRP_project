#! /usr/bin/env python

import unittest
import rostest
import rospy
from std_msgs.msg import Float64

bat=0
class MyTestCase(unittest.TestCase):

    def callback(self, data):
        bat=data.data


    def test_whatever(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("chatter", Float64, self.callback)
        self.assertTrue(bat<100)


if __name__ == "__main__":
    rostest.rosrun("spidy", "test_try", MyTestCase)
