# ROS2 Workspace (ros2_ws)

My ROS2 development workspace containing various robotics packages.

## 📦 Packages
- **my_py_pkg** - Python ROS2 nodes (publishers, subscribers, services)
- **my_cpp_pkg** - C++ ROS2 nodes  
- **my_robot_interfaces** - Custom messages and services
- **catch_them_all_turtlesim_pkg** - Turtlesim "Catch Them All" game
- **my_robot_bringup** - Launch files and configurations
- **my_bot** - Mobile robot simulation with Gazebo

## 🚀 Setup
```bash
# Clone
git clone https://github.com/ahmedashraf03/ros2_ws.git ~/ros2_ws

# Build
cd ~/ros2_ws
colcon build

# Source
source install/setup.bash

