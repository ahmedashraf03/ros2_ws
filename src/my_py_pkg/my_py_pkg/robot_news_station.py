#THIS is a PYTHON PUBLISHER NODE

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node):   
    def __init__(self):
        super().__init__("robot_news_station")
        self.declare_parameter("robot_name", "Hamo663Hamama")
        self.declare_parameter("timer_period", 1.0)  
        self.robot_name_ = self.get_parameter("robot_name").value
        self.timer_period_ = self.get_parameter("timer_period").value

        self.publisher_ = self.create_publisher(String,"robot_news",10)
        self.timer_ = self.create_timer(self.timer_period_,self.publish_news)
        self.get_logger().info("Robot News station has been started")

    def publish_news(self):
        msg = String()
        msg.data = "Hello this is " + self.robot_name_ + " From the robot news station."
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()   
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()