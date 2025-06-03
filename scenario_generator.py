import random
import time
from nuclear_crisis_simulation.models import ScenarioParameters

class ScenarioGenerator:
    SCENARIO_TEMPLATES = {
        "baltic": {
            "name": "Baltic Threshold",
            "description": "Russia employs tactical nuclear weapon against NATO forces in Baltic states",
            "base_parameters": {
                "escalation_position": "tactical",
                "nuclear_doctrine": "first_use"
            }
        },
        "pacific": {
            "name": "Pacific Signal",
            "description": "North Korea nuclear demonstration over international waters",
            "base_parameters": {
                "escalation_position": "demonstration",
                "nuclear_doctrine": "minimum"
            }
        },
        "cyber": {
            "name": "Cyber Nexus",
            "description": "Cyber attack on early warning systems with military mobilization",
            "base_parameters": {
                "escalation_position": "sub_strategic",
                "nuclear_doctrine": "first_use"
            }
        },
        "alliance": {
            "name": "Extended Deterrence Test",
            "description": "Nuclear threat against non-nuclear ally",
            "base_parameters": {
                "escalation_position": "strategic",
                "nuclear_doctrine": "extended"
            }
        }
    }

    def generate_scenario(self, scenario_type: str, variation: str = "A") -> ScenarioParameters:
        if scenario_type not in self.SCENARIO_TEMPLATES:
            raise ValueError(f"Unknown scenario type: {scenario_type}")
    
        template = self.SCENARIO_TEMPLATES[scenario_type]
        base_params = template["base_parameters"]
        variation_params = self._variation(variation)
    
        # Remove these lines because ScenarioParameters doesn't accept them
        # variation_params["scenario_name"] = template["name"]
        # variation_params["scenario_description"] = template["description"]
    
        variation_params.update(base_params)
        variation_params["scenario_type"] = scenario_type
    
        return ScenarioParameters(
            scenario_id=f"{scenario_type}_{variation}_{int(time.time())}",
            **variation_params
        )


    def _variation(self, v: str) -> dict:
        if v == "A":
            return {"threat_imminence": 4, "threat_magnitude": 4, "intelligence_confidence": 4,
                    "decision_time_pressure": 3, "alliance_consultation": 2, "domestic_pressure": 3,
                    "adversary_signaling": "clear"}
        elif v == "B":
            return {"threat_imminence": 2, "threat_magnitude": 4, "intelligence_confidence": 2,
                    "decision_time_pressure": 1, "alliance_consultation": 1, "domestic_pressure": 2,
                    "adversary_signaling": "mixed"}
        elif v == "C":
            return {"threat_imminence": 1, "threat_magnitude": 2, "intelligence_confidence": 4,
                    "decision_time_pressure": 1, "alliance_consultation": 1, "domestic_pressure": 4,
                    "adversary_signaling": "ambiguous"}
        else:
            return {k: random.randint(1, 4) for k in ["threat_imminence", "threat_magnitude",
                                                        "intelligence_confidence", "decision_time_pressure",
                                                        "alliance_consultation", "domestic_pressure"]}

