from enum import Enum

class ThreatLevel(Enum):
    LOW = 1
    MODERATE = 2
    HIGH = 3
    EXTREME = 4

class EscalationLevel(Enum):
    DIPLOMATIC = 1
    ECONOMIC = 2
    CONVENTIONAL_LIGHT = 3
    CONVENTIONAL_HEAVY = 4
    NUCLEAR_DEMONSTRATION = 5
    NUCLEAR_TACTICAL = 6
    NUCLEAR_LIMITED_STRATEGIC = 7
    NUCLEAR_STRATEGIC = 8
    NUCLEAR_MASSIVE = 9
    NUCLEAR_TOTAL = 10

class ResponseType(Enum):
    DIPLOMATIC = "diplomatic"
    ECONOMIC = "economic"
    CONVENTIONAL = "conventional"
    NUCLEAR = "nuclear"
