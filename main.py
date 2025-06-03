import json
import logging
from nuclear_crisis_simulation.scenario_generator import ScenarioGenerator
from nuclear_crisis_simulation.simulators.sole_authority import SoleAuthoritySimulator
from nuclear_crisis_simulation.simulators.war_council import WarCouncilSimulator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting simulation...")

    generator = ScenarioGenerator()
    scenario = generator.generate_scenario("baltic", "A")
    logger.info(f"Generated scenario: {scenario.to_dict()}")

    sole_sim = SoleAuthoritySimulator()
    council_sim = WarCouncilSimulator()

    logger.info(f"Running Sole Authority for scenario {scenario.scenario_id}")
    sole_result = sole_sim.run_simulation(scenario)
    logger.info(f"Sole Authority result: {sole_result.to_dict()}")

    with open(f"sole_result_{scenario.scenario_id}.json", "w") as f:
        json.dump(sole_result.to_dict(), f, indent=2)

    logger.info(f"Running War Council for scenario {scenario.scenario_id}")
    council_result = council_sim.run_simulation(scenario)
    logger.info(f"War Council result: {council_result.to_dict()}")

    with open(f"council_result_{scenario.scenario_id}.json", "w") as f:
        json.dump(council_result.to_dict(), f, indent=2)

    logger.info("Simulation complete. Results written to JSON files.")

if __name__ == "__main__":
    main()
