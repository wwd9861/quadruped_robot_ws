import rclpy as rp
from rclpy.node import Node
from sensor_msgs.msg import JointState

from math import *

l1, l2 = 220, 200


class LegCont(Node):
    def __init__(self):
        super().__init__("legcont")
        self.data = JointState()
        self.data.name = ["revolute1", "revolute2"]
        self.publisher = self.create_publisher(JointState, "/joint_states", 10)
        self.create_timer(0.1, self.timer_callback)
        self.t = 0

    def timer_callback(self):
        self.t += 0.2
        x, y = 100 * cos(self.t), -300 + 100 * sin(self.t)
        c2 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
        s2 = -sqrt(1 - c2**2)
        theta2 = atan2(s2, c2)
        theta1 = atan2(y, x) - atan2(l2 * s2, l1 + l2 * c2)

        theta2 = theta2 + 102 * pi / 180
        theta1 = theta1 + 30 * pi / 180
        self.data.position = [theta1, theta2]
        self.data.header.stamp = self.get_clock().now().to_msg()
        self.publisher.publish(self.data)


def main():
    rp.init()
    legcont = LegCont()
    rp.spin(legcont)

    legcont.destroy_node()
    rp.shutdown()


if __name__ == "__main__":
    main()
