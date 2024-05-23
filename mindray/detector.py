import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header

point = tuple[float, float, float]
quaternion = tuple[float, float, float, float]

class detector_node(Node):
    def __init__(self):
        super().__init__("detector_node")
        self.__sub = self.create_subscription(Image, "image/raw", self.__cb_image, 10)
        self.__pub = self.create_publisher(PoseStamped, "needle_pose", 10)
        self.cnt = 0.0

    def __cb_image(self, msg):
        bridge = CvBridge()
        frame = bridge.imgmsg_to_cv2(msg)
        # do something with the frame
        self.__publish_needle_pose(msg.header, (self.cnt, 0.0, 0.0), (1.0, 0.0, 0.0, 0.0))
        self.cnt += 1.0
        pass

    def __publish_needle_pose(self, header: Header, p: point, q: quaternion):
        '''
        Publish the needle pose to the needle_pose topic
        header: the header of the message
        p: the position of the needle
        q: the quaternion of the needle
        '''
        msg = PoseStamped()
        msg.header = header
        msg.pose.position.x = p[0]
        msg.pose.position.y = p[1]
        msg.pose.position.z = p[2]
        msg.pose.orientation.w = q[0]
        msg.pose.orientation.x = q[1]
        msg.pose.orientation.y = q[2]
        msg.pose.orientation.z = q[3]
        self.__pub.publish(msg)
        pass
    

def main(args=None):
    rclpy.init(args=args)
    node = detector_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
