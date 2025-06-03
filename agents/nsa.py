import random
from datetime import datetime
from nuclear_crisis_simulation.agents.base import CouncilAgent
from nuclear_crisis_simulation.models import ScenarioParameters, AgentDecision

class NSAAgent(CouncilAgent):
    def __init__(self):
        super().__init__(
            role="National Security Advisor",
            priorities=["Strategic coherence", "Risk management", "Policy coordination"],
            expertise=["Strategic planning", "Risk assessment", "Inter-agency coordination"]
        )

    def generate_initial_assessment(self, scenario: ScenarioParameters) -> AgentDecision:
        balanced_position = (scenario.threat_magnitude + scenario.threat_imminence) // 2 + 1
        return AgentDecision(
            agent_role=self.role,
            initial_position=balanced_position,
            final_position=balanced_position,
            confidence=5 + scenario.intelligence_confidence - 2,
            key_concerns=["Strategic coherence", "Risk management"],
            information_requests=["Comprehensive threat assessment", "Policy option analysis"],
            risk_assessment="Balanced risk assessment across multiple domains",
            justification="Strategic approach balances multiple considerations",
            position_changes=[]
        )

    def participate_discussion(self, other_positions, discussion_history):
        return "We need strategic coherence across our response options."

    def final_recommendation(self, discussion_summary, scenario: ScenarioParameters) -> AgentDecision:
        last_decision = self.position_history[-1] if self.position_history else 3
        final_position = max(1, min(10, last_decision + random.choice([-1, 0, 1])))
        return AgentDecision(
            agent_role=self.role,
            initial_position=last_decision,
            final_position=final_position,
            confidence=7,
            key_concerns=self.priorities[:2],
            information_requests=[],
            risk_assessment="Post-deliberation strategic assessment",
            justification="Ensuring strategic coherence",
            position_changes=[{"time": datetime.now().isoformat(), "position": final_position,
                               "reason": "Council deliberation"}]
        )
