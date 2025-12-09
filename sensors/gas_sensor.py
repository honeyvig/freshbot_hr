from freshbot_core.logger import log
import random

class GasSensor:
    def read_levels(self):
        # Simulated safe gas readings
        return {
            "TMA": round(random.uniform(0.1, 0.9), 2),
            "NH3": round(random.uniform(0.01, 0.4), 2),
            "H2S": round(random.uniform(0.01, 0.2), 2)
        }
