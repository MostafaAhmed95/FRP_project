# FRP_project

[![Build Status](https://travis-ci.com/MostafaAhmed95/FRP_project.svg?branch=tra_ci)](https://travis-ci.com/MostafaAhmed95/FRP_project)

just copy the spidy package into your work space <br/>
don't forget to catkin_make your work space after


at first launch the robot in gazebo using the following command<br/>
roslaunch spidy launch_gaz.launch


in a new terminal run the controller using the following command<br/>
roslaunch spidy rrbot_control.launch


after that you can write commands to move joints manually or use a python script<br/>
go to the directory spidy/py_messages  then run the python script there<br/>
python simple_pub.py


here is the video showing the steps and robot movment<br/>
https://www.youtube.com/watch?v=l6ctoMqnkRE&feature=youtu.be

after aproving the new request just type<br/>
roslaunch spidy all_launch.launch

here is the video showing the launch after adding the camera<br/>
https://youtu.be/r3qwlFgRL_4

you can find a folder called tests contain two python files<br/>
test_try.py for unit test<br/>
int_test.py for integration test

in the launch folder you could find<br/>
try_test.test which run the both tests unit and itegration<br/>
one_for_all.test which run both tests and all nodes needed


to run all the tests and nodes just type<br/>
rostest spidy one_for_all.test
