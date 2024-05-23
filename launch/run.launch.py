from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    capturer = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(
                    get_package_share_directory("mindray"),
                    "launch",
                    "capturer.launch.py",
                )
            ]
        ),
    )

    detector = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(
                    get_package_share_directory("mindray"),
                    "launch",
                    "detector.launch.py",
                )
            ]
        ),
    )
    return LaunchDescription(
        [
            capturer,
            detector,
        ]
    )
