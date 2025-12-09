import cv2
from freshbot_core.logger import log

class VisionSensor:
    def capture(self):
        log("Capturing simulated RGB image...")
        return cv2.imread("sample_fish.jpg")  # safe placeholder
