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
        #give false if our publisher has been publishing for long 
        self.assertTrue(bat<1000)


if __name__ == "__main__":
    rostest.rosrun("spidy", "test_try", MyTestCase)
