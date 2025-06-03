# Nuclear Crisis Decision-Making Simulation

This project simulates decision-making in hypothetical nuclear escalation scenarios. It’s a prototype system designed to model both **Sole Authority** decision-making (by a President) and **War Council** decision-making (by a group of national security leaders).

---

## How It Works

1. **Scenario Generation**  
   The simulation starts by generating a scenario based on a predefined template:
   - **Scenarios**: Baltic, Pacific, Cyber, Alliance  
   - **Intensity Variations**: A (high), B (moderate), C (low), or random  
   - Each scenario has a unique set of parameters (like threat magnitude, intelligence confidence, etc.).

2. **Sole Authority Simulation**  
   The **PresidentAgent** makes a decision based solely on the scenario parameters.  
   Outputs:
   - Final escalation level
   - Decision speed and confidence
   - Chosen response type (diplomatic, economic, conventional, nuclear)

3. **War Council Simulation**  
   A team of agents (President, SecDef, SecState, NSA, CJCS) each form their own assessments.  
   - **3 rounds of deliberation** refine these positions.  
   - Final decisions reflect group dynamics and consensus-building.

4. **Output**  
   Results for both simulations are saved as `.json` files:
   - `sole_result_<scenario_id>.json`
   - `council_result_<scenario_id>.json`

---

## 📂 Project Structure

```plaintext
nuclear_crisis_simulation/
├── __init__.py
├── main.py                  # Entry point for running a simulation
├── scenario_generator.py    # Defines scenario templates and randomization
├── models.py                # Data models (ScenarioParameters, AgentDecision, etc.)
├── agents/
│   ├── __init__.py
│   ├── base.py              # Abstract CouncilAgent class
│   ├── president.py         # PresidentAgent logic
│   ├── secdef.py            # Secretary of Defense logic
│   ├── secstate.py          # Secretary of State logic
│   ├── nsa.py               # National Security Advisor logic
│   └── cjcs.py              # Chairman of Joint Chiefs logic
└── simulators/
    ├── __init__.py
    ├── sole_authority.py    # Sole Authority simulator
    └── war_council.py       # War Council simulator



## System Overview

+------------------------------------------+
|        NUCLEAR CRISIS SIMULATION         |
+------------------------------------------+
|         Scenario Generator                |
|      (variation A/B/C/random)            |
|------------------------------------------|
|         Sole Authority Simulator         |
|  - President's decision based on         |
|    scenario factors                      |
|  - Produces final escalation level       |
+------------------------------------------+
|         War Council Simulator            |
|  - President                             |
|  - SecDef                                |
|  - SecState                              |
|  - NSA                                   |
|  - CJCS                                  |
|                                          |
|  - 3 rounds of discussion                |
|  - Final group decision (consensus?)     |
+------------------------------------------+
|  Results:                                |
|   - Sole Authority Decision              |
|   - War Council Decision                 |
|   - Group dynamics metrics               |
|   - Written to JSON files                |
+------------------------------------------+
