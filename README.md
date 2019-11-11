# FRP_project
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


