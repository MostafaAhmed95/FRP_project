# FRP_project
just copy the spidy package into your work space 
don't forget to catkin_make your work space after

at first launch the robot in gazebo using the following command 
roslaunch spidy launch_gaz.launch 

in a new terminal run the controller using the following command
roslaunch spidy rrbot_control.launch

after that you can write commands to move joints manualu or use a python script
go to the directory spidy/py_messages  then run the python script there
python simple_pub.py
