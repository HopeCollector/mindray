from setuptools import find_packages, setup
import os
from glob import glob

package_name = "mindray"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*launch.[pxy][yma]*")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="root",
    maintainer_email="cmw4187@icloud.com",
    description="convert hdmi to sensor_msgs/Image and sensor_msgs/CompressedImage msg stream",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "capturer = mindray.capturer:main",
            "detector = mindray.detector:main",
        ],
    },
)
