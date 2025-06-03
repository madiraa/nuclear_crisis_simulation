import random
from datetime import datetime
from nuclear_crisis_simulation.agents.base import CouncilAgent
from nuclear_crisis_simulation.models import ScenarioParameters, AgentDecision

class SecDefAgent(CouncilAgent):
    def __init__(self):
        super().__init__(
            role="Secretary of Defense",
            priorities=["Military effectiveness", "Force protection", "Operational feasibility"],
            expertise=["Nuclear doctrine", "Military capabilities", "Force readiness"]
        )

    def generate_initial_assessment(self, scenario: ScenarioParameters) -> AgentDecision:
        military_bias = 1 if scenario.intelligence_confidence >= 3 else 0
        threat_response = scenario.threat_magnitude + military_bias
        initial_position = max(2, min(8, threat_response + 1))

        concerns = ["Force protection", "Military effectiveness"]
        if scenario.decision_time_pressure >= 3:
            concerns.append("Limited time for force positioning")
        if scenario.threat_magnitude >= 3:
            concerns.append("Escalation control")

        requests = ["Enemy force disposition", "Allied military capabilities"]
        if scenario.escalation_position in ["tactical", "strategic"]:
            requests.append("Nuclear weapon readiness status")

        risk = ("High operational risk, potential for casualties" if scenario.threat_magnitude >= 3
                else "Moderate operational risk within acceptable parameters")

        return AgentDecision(
            agent_role=self.role,
            initial_position=initial_position,
            final_position=initial_position,
            confidence=7 + scenario.intelligence_confidence - 2,
            key_concerns=concerns,
            information_requests=requests,
            risk_assessment=risk,
            justification=f"Military response level {initial_position} provides appropriate deterrent effect",
            position_changes=[]
        )

    def participate_discussion(self, other_positions, discussion_history):
        return "Military feasibility supports range of options from conventional to limited nuclear response."

    def final_recommendation(self, discussion_summary, scenario: ScenarioParameters) -> AgentDecision:
        last_decision = self.position_history[-1] if self.position_history else 4
        final_position = max(1, min(10, last_decision + random.choice([-1, 0, 1])))
        return AgentDecision(
            agent_role=self.role,
            initial_position=last_decision,
            final_position=final_position,
            confidence=8,
            key_concerns=self.priorities[:2],
            information_requests=[],
            risk_assessment="Post-deliberation military assessment",
            justification="Maintaining military readiness with limited escalation",
            position_changes=[{"time": datetime.now().isoformat(), "position": final_position,
                               "reason": "Council deliberation"}]
        )
