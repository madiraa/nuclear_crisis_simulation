import time
from nuclear_crisis_simulation.agents.president import PresidentAgent
from nuclear_crisis_simulation.models import ScenarioParameters, SimulationResult

class SoleAuthoritySimulator:
    def __init__(self):
        self.president = PresidentAgent()

    def run_simulation(self, scenario: ScenarioParameters) -> SimulationResult:
        start_time = time.time()
        decision = self.president.generate_initial_assessment(scenario)
        decision_time = time.time() - start_time
        return SimulationResult(
            simulation_id=f"sole_{scenario.scenario_id}_{int(time.time())}",
            scenario_parameters=scenario,
            authority_type="sole",
            final_escalation_level=decision.final_position,
            decision_speed_minutes=decision_time / 60,
            decision_confidence=decision.confidence,
            response_type=self._determine_response_type(decision.final_position),
            agent_behaviors={"president": decision},
            process_metrics={
                "deliberation_time": decision_time / 60,
                "information_requests": len(decision.information_requests),
                "position_changes": len(decision.position_changes)
            }
        )

    def _determine_response_type(self, escalation_level: int) -> str:
        if escalation_level <= 2: return "diplomatic"
        elif escalation_level <= 4: return "economic"
        elif escalation_level <= 6: return "conventional"
        else: return "nuclear"
