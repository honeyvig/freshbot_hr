from sensors.gas_sensor import GasSensor
from sensors.temperature_sensor import TemperatureSensor
from sensors.vision_sensor import VisionSensor

from ai_models.freshness_cnn import FreshnessCNN
from ai_models.gas_rnn_predictor import GasRNNPredictor
from ai_models.coldchain_rl import ColdChainRL
from ai_models.llm_brain import LLMBrain

from robot_actions.clean_fish import clean_fish
from robot_actions.apply_brine import apply_brine
from robot_actions.package_fish import package_fish
from robot_actions.uv_sanitize import sanitize

from freshbot_core.logger import log

def run_once():
    log("===== FRESHBOT-HR CYCLE STARTED =====")

    gas = GasSensor().read_levels()
    temp = TemperatureSensor().read()
    image = VisionSensor().capture()

    freshness = FreshnessCNN().predict(image)
    spoilage = GasRNNPredictor().predict_spoilage(gas, temp)
    cold_chain = ColdChainRL().optimize(temp, gas)
    decision = LLMBrain().decide(freshness, gas, temp)

    log(f"Freshness Score: {freshness}")
    log(f"Gas Levels: {gas}")
    log(f"Decision: {decision}")

    if decision == "CLEAN_AND_DEODORIZE":
        clean_fish()
        apply_brine()
        sanitize()
    elif decision == "DISCARD":
        log("Fish discarded.")
    else:
        package_fish()

    log("===== CYCLE COMPLETE =====")
