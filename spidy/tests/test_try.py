#! /usr/bin/env python

import unittest
import rostest
import rospy
from std_msgs.msg import Float64



bat=0
class MyTestCase(unittest.TestCase):

    def callback(self, data):
        #get that from the topic that publish joint state
        pub_value=data.data

    def callback_state(self,data)
        #get the state of the robot
        rec_value=data.set_point

    def test_whatever(self):
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber("/rrbot/joint1_position_controller/command", Float64, self.callback)
        rospy.Subscriber("/rrbot/joint1_position_controller/state", Float64, self.callback_state)
        #compare them  to see if my command applied or not
        self.assertTrue(pub_value==rec_value)


if __name__ == "__main__":
    rostest.rosrun("spidy", "test_try", MyTestCase)
