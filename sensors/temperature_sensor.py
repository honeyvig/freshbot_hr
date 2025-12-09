from freshbot_core.logger import log
import random

class TemperatureSensor:
    def read(self):
        return round(random.uniform(0.5, 6.0), 2)
