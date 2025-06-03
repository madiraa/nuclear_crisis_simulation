import random
from datetime import datetime
from nuclear_crisis_simulation.agents.base import CouncilAgent
from nuclear_crisis_simulation.models import ScenarioParameters, AgentDecision
from typing import List

class PresidentAgent(CouncilAgent):
    def __init__(self):
        super().__init__(
            role="President",
            priorities=["National survival", "Political viability", "Alliance credibility", "Constitutional constraints"],
            expertise=["Strategic decision-making", "Political consequences", "Constitutional authority"]
        )

    def generate_initial_assessment(self, scenario: ScenarioParameters) -> AgentDecision:
        threat_weight = scenario.threat_magnitude * 2
        imminence_weight = scenario.threat_imminence * 1.5
        confidence_adjustment = scenario.intelligence_confidence * 0.5
        base_level = int((threat_weight + imminence_weight + confidence_adjustment) / 2)
        domestic_modifier = 1 if scenario.domestic_pressure >= 3 else -1 if scenario.domestic_pressure == 1 else 0
        alliance_modifier = 1 if scenario.alliance_consultation <= 2 else 0
        initial_position = max(1, min(10, base_level + domestic_modifier + alliance_modifier))

        concerns = []
        if scenario.threat_magnitude >= 3: concerns.append("Existential threat to national security")
        if scenario.domestic_pressure >= 3: concerns.append("Domestic political pressure for strong response")
        if scenario.alliance_consultation <= 2: concerns.append("Limited time for allied consultation")
        if scenario.intelligence_confidence <= 2: concerns.append("Uncertain intelligence picture")

        confidence = max(1, min(10, 5 + scenario.intelligence_confidence - 2 - (4 - scenario.decision_time_pressure)))
        requests = []
        if scenario.intelligence_confidence <= 2: requests.append("Additional intelligence verification")
        if scenario.alliance_consultation >= 2: requests.append("Allied government positions")
        if scenario.threat_magnitude >= 3: requests.append("Casualty estimates for response options")

        risk = ("High risk of escalation spiral" if scenario.threat_magnitude >= 3 else
                "Moderate risk of regional instability" if scenario.threat_magnitude == 2 else
                "Low risk, primarily diplomatic consequences")
        justifications = {1: "Diplomatic engagement remains the best path forward",
                          2: "Economic pressure can achieve objectives without military risk",
                          3: "Limited conventional response demonstrates resolve",
                          4: "Substantial conventional response required for deterrence",
                          5: "Nuclear demonstration necessary to prevent escalation",
                          6: "Tactical nuclear response proportionate to threat",
                          7: "Limited strategic response required for national survival",
                          8: "Strategic nuclear response necessary",
                          9: "Massive response required for regime survival",
                          10: "Total nuclear response for national survival"}
        justification = justifications.get(initial_position, "Response proportionate to threat level")

        return AgentDecision(
            agent_role=self.role,
            initial_position=initial_position,
            final_position=initial_position,
            confidence=confidence,
            key_concerns=concerns,
            information_requests=requests,
            risk_assessment=risk,
            justification=justification,
            position_changes=[]
        )

    def participate_discussion(self, other_positions: List[AgentDecision], discussion_history: List[str]) -> str:
        avg_recommendation = sum(pos.final_position for pos in other_positions) / len(other_positions)
        if abs(self.position_history[-1] - avg_recommendation) > 2:
            return f"I'm concerned about the range of recommendations."
        else:
            return "General alignment in our recommendations. Let's finalize."

    def final_recommendation(self, discussion_summary: str, scenario: ScenarioParameters) -> AgentDecision:
        last_decision = self.position_history[-1] if self.position_history else 5
        adjustment = random.choice([-1, 0, 1])
        final_position = max(1, min(10, last_decision + adjustment))
        return AgentDecision(
            agent_role=self.role,
            initial_position=self.position_history[0] if self.position_history else 5,
            final_position=final_position,
            confidence=8,
            key_concerns=["National security", "Political consequences"],
            information_requests=[],
            risk_assessment="Acceptable risk level for chosen response",
            justification="Final decision balances security needs with political realities",
            position_changes=[{"time": datetime.now().isoformat(), "position": final_position,
                               "reason": "Council deliberation"}]
        )
