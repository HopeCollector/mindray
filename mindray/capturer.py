from .hdmi import hdmi_device
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge

class capturer_node(Node):
    def __init__(self):
        super().__init__('capturer_node')
        dev = self.declare_parameter('device', '/dev/video4').get_parameter_value().string_value
        width = self.declare_parameter('width', 1920).get_parameter_value().integer_value
        height = self.declare_parameter('height', 1080).get_parameter_value().integer_value
        fps = self.declare_parameter('fps', 60).get_parameter_value().integer_value
        self.__dev = hdmi_device(dev, width, height, fps)
        self.__pub_raw = self.create_publisher(Image, 'image/raw', 10)
        self.__pub_comressed = self.create_publisher(CompressedImage, 'image/compressed', 10)
        self.__timer_60hz = self.create_timer(1/60, self.__cb_60hz)
    
    def destroy_node(self):
        self.__dev.close()
        super().destroy_node()

    def __cb_60hz(self):
        ret, frame = self.__dev.capture()
        if not ret:
            self.get_logger().error("Failed to capture frame")
            return
        bridge = CvBridge()
        imgmsg = bridge.cv2_to_imgmsg(frame)
        imgmsg.header.stamp = self.get_clock().now().to_msg()
        imgmsg.header.frame_id = "mindray"
        self.__pub_raw.publish(imgmsg)
        imgmsg = bridge.cv2_to_compressed_imgmsg(frame)
        self.__pub_comressed.publish(imgmsg)
        pass

def main(args=None):
    rclpy.init(args=args)
    node = capturer_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
