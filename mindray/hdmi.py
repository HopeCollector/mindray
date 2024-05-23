import cv2
import sys
import time


class hdmi_device:
    def __init__(self, device: str, width: int, height: int, fps: int = 30):
        self.__cap = cv2.VideoCapture()
        self.__dev = device
        self.__width = width
        self.__height = height
        self.__fps = fps
        self.open()

    def __del__(self):
        self.close()

    def open(self) -> bool:
        ret = False
        if self.__cap.open(self.__dev):
            self.__cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.__width)
            self.__cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.__height)
            self.__cap.set(cv2.CAP_PROP_FPS, self.__fps)
            ret = True
        return ret

    def close(self):
        if self.__cap.isOpened():
            self.__cap.release()

    def reopen(self) -> bool:
        self.close()
        time.sleep(2)
        return self.open()

    def is_open(self) -> bool:
        return self.__cap.isOpened()

    def capture(self, try_time: int = 5) -> tuple[bool, cv2.typing.MatLike]:
        for i in range(try_time):
            try:
                ret, frame = self.__cap.read()
                return ret, frame
            except Exception as e:
                # print(f"Failed to read frame, retry {i}/{try_time}")
                self.reopen()
        return False, cv2.Mat([0])


if __name__ == "__main__":
    dev = hdmi_device("/dev/video4", 1920, 1080, 60)
    if not dev.open():
        print("Failed to open device")
        sys.exit(1)

    while True:
        ret, frame = dev.capture()
        if not ret:
            print("Failed to capture frame")
            break
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
