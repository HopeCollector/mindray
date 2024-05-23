from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="mindray",
                namespace="mindray",
                executable="detector",
                name="detector_node",
                output="screen",
            ),
        ]
    )
