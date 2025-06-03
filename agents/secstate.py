import random
from datetime import datetime
from nuclear_crisis_simulation.agents.base import CouncilAgent
from nuclear_crisis_simulation.models import ScenarioParameters, AgentDecision

class SecStateAgent(CouncilAgent):
    def __init__(self):
        super().__init__(
            role="Secretary of State",
            priorities=["Alliance cohesion", "International law", "Diplomatic solutions"],
            expertise=["International relations", "Treaty obligations", "Diplomatic channels"]
        )

    def generate_initial_assessment(self, scenario: ScenarioParameters) -> AgentDecision:
        diplomatic_preference = -2
        alliance_factor = 1 if scenario.alliance_consultation <= 2 else 0
        initial_position = max(1, min(6, scenario.threat_magnitude + diplomatic_preference + alliance_factor))

        concerns = ["Alliance unity", "International law compliance"]
        if scenario.alliance_consultation <= 2:
            concerns.append("Insufficient allied consultation")

        requests = ["Allied government positions", "International legal constraints", "Diplomatic channels available"]

        risk = "Risk of alliance fracture and international isolation with high escalation"

        return AgentDecision(
            agent_role=self.role,
            initial_position=initial_position,
            final_position=initial_position,
            confidence=6 + scenario.alliance_consultation - 2,
            key_concerns=concerns,
            information_requests=requests,
            risk_assessment=risk,
            justification=f"Diplomatic approach at level {initial_position} preserves international relationships",
            position_changes=[]
        )

    def participate_discussion(self, other_positions, discussion_history):
        return "We must consider international law and alliance cohesion in our response."

    def final_recommendation(self, discussion_summary, scenario: ScenarioParameters) -> AgentDecision:
        last_decision = self.position_history[-1] if self.position_history else 2
        final_position = max(1, min(10, last_decision + random.choice([-1, 0, 1])))
        return AgentDecision(
            agent_role=self.role,
            initial_position=last_decision,
            final_position=final_position,
            confidence=7,
            key_concerns=self.priorities[:2],
            information_requests=[],
            risk_assessment="Post-deliberation diplomatic assessment",
            justification="Preserving international relationships",
            position_changes=[{"time": datetime.now().isoformat(), "position": final_position,
                               "reason": "Council deliberation"}]
        )
