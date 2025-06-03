from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

@dataclass
class ScenarioParameters:
    scenario_id: str
    threat_imminence: int
    threat_magnitude: int
    intelligence_confidence: int
    decision_time_pressure: int
    alliance_consultation: int
    domestic_pressure: int
    adversary_signaling: str
    escalation_position: str
    nuclear_doctrine: str
    scenario_type: str

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class AgentDecision:
    agent_role: str
    initial_position: int
    final_position: int
    confidence: int
    key_concerns: List[str]
    information_requests: List[str]
    risk_assessment: str
    justification: str
    position_changes: List[Dict]

@dataclass
class SimulationResult:
    simulation_id: str
    scenario_parameters: ScenarioParameters
    authority_type: str
    final_escalation_level: int
    decision_speed_minutes: float
    decision_confidence: int
    response_type: str
    agent_behaviors: Dict[str, AgentDecision]
    group_dynamics: Optional[Dict] = None
    process_metrics: Dict = None

    def to_dict(self) -> Dict:
        result = asdict(self)
        result["scenario_parameters"] = self.scenario_parameters.to_dict()
        return result
