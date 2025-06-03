import random
from datetime import datetime
from nuclear_crisis_simulation.agents.base import CouncilAgent
from nuclear_crisis_simulation.models import ScenarioParameters, AgentDecision

class CJCSAgent(CouncilAgent):
    def __init__(self):
        super().__init__(
            role="Chairman of Joint Chiefs",
            priorities=["Military advice", "Service member protection", "Military doctrine"],
            expertise=["Military strategy", "Operational planning", "Force readiness"]
        )

    def generate_initial_assessment(self, scenario: ScenarioParameters) -> AgentDecision:
        doctrine_position = scenario.threat_magnitude + (1 if scenario.nuclear_doctrine == "first_use" else 0)
        initial_position = min(7, doctrine_position)
        return AgentDecision(
            agent_role=self.role,
            initial_position=initial_position,
            final_position=initial_position,
            confidence=7,
            key_concerns=["Military doctrine adherence", "Force protection"],
            information_requests=["Force readiness status", "Operational constraints"],
            risk_assessment="Military risk assessment based on current readiness",
            justification="Military recommendation based on doctrine and capabilities",
            position_changes=[]
        )

    def participate_discussion(self, other_positions, discussion_history):
        return "Military capabilities support the recommended response levels."

    def final_recommendation(self, discussion_summary, scenario: ScenarioParameters) -> AgentDecision:
        last_decision = self.position_history[-1] if self.position_history else 4
        final_position = max(1, min(10, last_decision + random.choice([-1, 0, 1])))
        return AgentDecision(
            agent_role=self.role,
            initial_position=last_decision,
            final_position=final_position,
            confidence=7,
            key_concerns=self.priorities[:2],
            information_requests=[],
            risk_assessment="Post-deliberation military assessment",
            justification="Aligning military advice with council consensus",
            position_changes=[{"time": datetime.now().isoformat(), "position": final_position,
                               "reason": "Council deliberation"}]
        )
