class LLMBrain:
    def decide(self, freshness, gas, temp):
        if freshness < 0.5:
            return "DISCARD"
        if gas["TMA"] > 0.7:
            return "CLEAN_AND_DEODORIZE"
        return "OK"
