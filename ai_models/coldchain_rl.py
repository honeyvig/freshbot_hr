class ColdChainRL:
    def optimize(self, temp, gas_levels):
        if temp > 4:
            return "COOL_DOWN"
        return "STABLE"
