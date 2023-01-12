Fizikalni simulator mobilnog robota Turtlebot3 gdje se pomocu LIDAR-a mapira prostor i lokalizira robot u istom (SLAM algoritam - gmapping). 

Pokretanjem naredba u Terminal-u se moze omoguciti autonomna navigacija u prethodno spremljenoj mapi prostora (kuca):

Tab 1: ' $ roslaunch turtlebot3_gazebo turtlebot3_house.launch '

Tab 2: ' $ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/vjezba2/map.yaml '
