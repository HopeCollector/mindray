# mindray

一个基于 ros2 的视频串流与特征检测项目

## 安装

```shell
# clone
$ cd ~/ros2_ws/src
$ git clone https://github.com/HopeCollector/mindray.git

# dependencies
$ cd mindray
$ pip3 install -r requirements.txt

# colcon
$ cd ~/ros2_ws
$ colcon build --symlink-install --base-paths src
```

## 运行

视频采集设备在 `/dev/video0`, 分辨率为 `720x480`, 10 fps 

- 启动所有节点
```shell
ros2 launch mindray run.launch.py \
    device:=/dev/video0 \
    width:=720 height:=480 \
    fps:=10
```

- 启动串流节点
```shell
ros2 launch mindray capturer.launch.py \
    device:=/dev/video0 \
    width:=720 height:=480 \
    fps:=10
```

- 启动目标检测节点
```shell
ros2 launch mindray detector.launch.py
```
