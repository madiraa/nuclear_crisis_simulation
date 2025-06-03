import time
import random
from statistics import stdev, mean
from nuclear_crisis_simulation.agents import PresidentAgent, SecDefAgent, SecStateAgent, NSAAgent, CJCSAgent
from nuclear_crisis_simulation.models import ScenarioParameters, SimulationResult

class WarCouncilSimulator:
    def __init__(self):
        self.agents = {
            "president": PresidentAgent(),
            "secdef": SecDefAgent(),
            "secstate": SecStateAgent(),
            "nsa": NSAAgent(),
            "cjcs": CJCSAgent()
        }
        self.discussion_log = []

    def run_simulation(self, scenario: ScenarioParameters) -> SimulationResult:
        start_time = time.time()
        initial_positions = {r: a.generate_initial_assessment(scenario) for r, a in self.agents.items()}
        for r, a in self.agents.items():
            a.position_history.append(initial_positions[r].initial_position)

        # Deliberation
        for _ in range(3):
            for role, agent in self.agents.items():
                others = [p for r2, p in initial_positions.items() if r2 != role]
                statement = agent.participate_discussion(others, self.discussion_log)
                self.discussion_log.append(f"{role}: {statement}")

        final_positions = {}
        for role, agent in self.agents.items():
            final_positions[role] = agent.final_recommendation("\n".join(self.discussion_log[-5:]), scenario)

        decision_time = time.time() - start_time
        final_escalation = final_positions["president"].final_position

        return SimulationResult(
            simulation_id=f"council_{scenario.scenario_id}_{int(time.time())}",
            scenario_parameters=scenario,
            authority_type="council",
            final_escalation_level=final_escalation,
            decision_speed_minutes=decision_time / 60,
            decision_confidence=final_positions["president"].confidence,
            response_type=self._determine_response_type(final_escalation),
            agent_behaviors=final_positions,
            group_dynamics={"consensus_level": self._calculate_consensus_level(final_positions)},
            process_metrics={
                "deliberation_time": decision_time / 60,
                "total_statements": len(self.discussion_log)
            }
        )

    def _calculate_consensus_level(self, final_positions: dict) -> int:
        positions = [pos.final_position for pos in final_positions.values()]
        return max(1, 10 - (max(positions) - min(positions)))

    def _determine_response_type(self, escalation_level: int) -> str:
        if escalation_level <= 2: return "diplomatic"
        elif escalation_level <= 4: return "economic"
        elif escalation_level <= 6: return "conventional"
        else: return "nuclear"
