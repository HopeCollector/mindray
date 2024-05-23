from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument("device", default_value="/dev/video4"),
            DeclareLaunchArgument("width", default_value="1920"),
            DeclareLaunchArgument("height", default_value="1080"),
            DeclareLaunchArgument("fps", default_value="60"),
            Node(
                package="mindray",
                namespace="mindray",
                executable="capturer",
                name="capturer_node",
                parameters=[
                    {"device": LaunchConfiguration("device")},
                    {"width": LaunchConfiguration("width")},
                    {"height": LaunchConfiguration("height")},
                    {"fps": LaunchConfiguration("fps")},
                ],
            ),
        ]
    )
